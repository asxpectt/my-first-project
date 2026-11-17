"""Fix and repackage the UIverse HUD Kit.

Reads the kit as XML (made from the .rbxm by the rbx-dom converter), applies the fixes
below, and writes two XML files that the converter turns into binary:
  - place.rbxlx : a ready-to-play place with everything in its real service
  - kit.rbxmx   : the same kit as an insertable model (same folder layout as the original)

Fixes:
  1. Both UIPackServer and MainHUD's HUDServer set MarketplaceService.ProcessReceipt.
     Roblox keeps only the last one, so one system's purchases were never granted.
     Now both register with one ReceiptRouter.
  2. HUDServer pays rewards (daily, time, codes, wheel, group, gifts) into leaderstats.Cash,
     but UIPackServer overwrote leaderstats.Cash from its own data on every sync, wiping them.
     UIPackServer now adds outside changes to leaderstats.Cash into its own data.
  3. HUDServer no longer resets an existing leaderstats.Cash to its own saved value.
  4. BonusCash (a 1,000,000 cash gift to every new player) is turned off for a real game.

Usage: python3 -I build_hud.py <kit.rbxmx> <out_dir>
"""

import copy
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROUTER = """-- ReceiptRouter: the single MarketplaceService.ProcessReceipt for this game.
-- Roblox allows only one ProcessReceipt. This kit has two purchase systems
-- (UIPackServer and MainHUD's HUDServer), so each one adds a handler here.
-- A handler returns a ProductPurchaseDecision for its own products, or nil if the
-- product isn't one of its own, so the next handler can try.
local MarketplaceService = game:GetService("MarketplaceService")

local handlers = {}

MarketplaceService.ProcessReceipt = function(info)
	for _, handler in handlers do
		local ok, decision = pcall(handler, info)
		if not ok then
			warn("[ReceiptRouter]", decision)
			return Enum.ProductPurchaseDecision.NotProcessedYet -- Roblox retries later
		end
		if decision ~= nil then
			return decision
		end
	end
	return Enum.ProductPurchaseDecision.NotProcessedYet
end

return {
	add = function(handler)
		table.insert(handlers, handler)
	end,
}
"""

REQUIRE_ROUTER = 'require(game:GetService("ServerScriptService"):WaitForChild("ReceiptRouter")).add(function('

PATCHES = {
    "UIPackServer": [
        (
            "MarketplaceService.ProcessReceipt = function(info)",
            REQUIRE_ROUTER + "info)",
        ),
        (
            "\t\t\treturn Enum.ProductPurchaseDecision.PurchaseGranted\n\t\tend\n\tend\n"
            "\treturn Enum.ProductPurchaseDecision.NotProcessedYet\nend\n",
            "\t\t\treturn Enum.ProductPurchaseDecision.PurchaseGranted\n\t\tend\n\tend\n"
            "\treturn nil -- not one of ours: let the next handler try\nend)\n",
        ),
        (
            "local passCache = {} -- [player] = { [passKey] = true }\n",
            "local passCache = {} -- [player] = { [passKey] = true }\n"
            'local lastCash = setmetatable({}, { __mode = "k" }) -- [player] = Cash we last wrote to leaderstats\n',
        ),
        (
            "\t\tif cash then cash.Value = d.Cash end\n",
            "\t\tif cash then\n\t\t\tlastCash[p] = d.Cash\n\t\t\tcash.Value = d.Cash\n\t\tend\n",
        ),
        (
            '\tp:SetAttribute("FriendBoost", friendBoost(p))\n',
            "\t-- Other scripts (MainHUD rewards, codes, wheel...) add to leaderstats.Cash directly.\n"
            "\t-- Add those changes to our data so sync() doesn't wipe them.\n"
            '\tls.Cash.Changed:Connect(function(v)\n'
            "\t\tlocal d2 = data[p]\n"
            "\t\tif not d2 or lastCash[p] == nil or v == lastCash[p] then return end\n"
            "\t\td2.Cash += v - lastCash[p]\n"
            "\t\tsync(p)\n"
            "\tend)\n"
            '\tp:SetAttribute("FriendBoost", friendBoost(p))\n',
        ),
    ],
    "HUDServer": [
        (
            "MarketplaceService.ProcessReceipt = function(receipt)",
            REQUIRE_ROUTER + "receipt)",
        ),
        (
            "\tif not player or not key or not data[player] then return Enum.ProductPurchaseDecision.NotProcessedYet end\n",
            "\tif not key then return nil end -- not one of ours: let the next handler try\n"
            "\tif not player or not data[player] then return Enum.ProductPurchaseDecision.NotProcessedYet end\n",
        ),
        (
            "\tsave(player)\n\treturn Enum.ProductPurchaseDecision.PurchaseGranted\nend\n"
            "MarketplaceService.PromptGamePassPurchaseFinished",
            "\tsave(player)\n\treturn Enum.ProductPurchaseDecision.PurchaseGranted\nend)\n"
            "MarketplaceService.PromptGamePassPurchaseFinished",
        ),
        (
            '\tlocal cash = leaderstats:FindFirstChild("Cash") or Instance.new("NumberValue")\n'
            '\tcash.Name = "Cash"\n\tcash.Value = d.Cash\n',
            '\tlocal existing = leaderstats:FindFirstChild("Cash")\n'
            '\tlocal cash = existing or Instance.new("NumberValue")\n'
            '\tcash.Name = "Cash"\n'
            "\tif not existing then cash.Value = d.Cash end -- UIPackServer owns Cash when it made it first\n",
        ),
    ],
    "Config": [
        (
            "C.BonusCash = 1000000 -- one-time gift to every player (0 = off)",
            "C.BonusCash = 0 -- one-time gift to every player (0 = off). The kit shipped with 1000000 for testing.",
        ),
    ],
}

README_NOTE = """
======================================================
FIXED VERSION (repackaged)
- ServerScriptService > ReceiptRouter is new. Move it into
  ServerScriptService with UIPackServer. Both purchase
  systems now share it (Roblox allows only one
  ProcessReceipt, so before this one system's purchases
  were never granted).
- Rewards from the MainHUD windows (daily, time, codes,
  wheel, group) now stay on your cash instead of being
  overwritten.
- BonusCash is set to 0.
======================================================
"""

_ref = [0]


def ref():
    _ref[0] += 1
    return f"RBXFIX{_ref[0]}"


def props(item):
    return item.find("Properties")


def get(item, name):
    for p in props(item):
        if p.get("name") == name:
            return p
    return None


def name_of(item):
    return get(item, "Name").text


def child(item, name):
    for c in item.findall("Item"):
        if name_of(c) == name:
            return c
    raise KeyError(name)


def new_item(cls, name, extra=None):
    it = ET.Element("Item", {"class": cls, "referent": ref()})
    pr = ET.SubElement(it, "Properties")
    n = ET.SubElement(pr, "string", {"name": "Name"})
    n.text = name
    for el in extra or []:
        pr.append(el)
    return it


def el(tag, name, text=None, **children):
    e = ET.Element(tag, {"name": name})
    if text is not None:
        e.text = text
    for k, v in children.items():
        ET.SubElement(e, k).text = str(v)
    return e


def part(cls, name, pos, size, color, material=256):
    cf = {"X": pos[0], "Y": pos[1], "Z": pos[2],
          "R00": 1, "R01": 0, "R02": 0, "R10": 0, "R11": 1, "R12": 0, "R20": 0, "R21": 0, "R22": 1}
    extra = [
        el("bool", "Anchored", "true"),
        el("bool", "Locked", "true"),
        el("CoordinateFrame", "CFrame", **cf),
        el("Vector3", "size", X=size[0], Y=size[1], Z=size[2]),
        el("Color3uint8", "Color3uint8", str((255 << 24) | (color[0] << 16) | (color[1] << 8) | color[2])),
        el("token", "Material", str(material)),
    ]
    if cls == "SpawnLocation":
        extra.append(el("int", "Duration", "0"))  # no spawn force field
    return new_item(cls, name, extra)


def script_items(root):
    for it in root.iter("Item"):
        if it.get("class") in ("Script", "LocalScript", "ModuleScript"):
            yield it


def patch_sources(root):
    done = set()
    for it in script_items(root):
        n = name_of(it)
        if n in PATCHES:
            src_el = get(it, "Source")
            src = src_el.text or ""
            for old, new in PATCHES[n]:
                count = src.count(old)
                if count != 1:
                    sys.exit(f"patch for {n} matched {count} times, expected 1:\n{old[:120]}")
                src = src.replace(old, new)
            src_el.text = src
            done.add(n)
        if n == "README - START HERE":
            s = get(it, "Source")
            s.text = (s.text or "").replace("]]", README_NOTE + "]]", 1)
    missing = set(PATCHES) - done
    if missing:
        sys.exit(f"scripts not found: {missing}")


def router_item():
    return new_item("ModuleScript", "ReceiptRouter", [el("ProtectedString", "Source", ROUTER)])


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    tree = ET.parse(src)
    root = tree.getroot()
    patch_sources(root)

    kit = root.find("Item")  # the "UIverse UI Pack" Model
    child(kit, "ServerScriptService").append(router_item())

    # 1) fixed insertable model, same layout as the original
    tree.write(out / "kit.rbxmx", encoding="utf-8", xml_declaration=False)

    # 2) ready-to-play place: each folder's contents go into the real service
    place = ET.Element("roblox", {"version": "4"})
    services = {}

    def service(cls):
        if cls not in services:
            services[cls] = new_item(cls, cls)
            place.append(services[cls])
        return services[cls]

    folders = {
        "ReplicatedStorage": "ReplicatedStorage",
        "ServerScriptService": "ServerScriptService",
        "StarterGui": "StarterGui",
        "Workspace": "Workspace",
    }
    for folder, cls in folders.items():
        for c in child(kit, folder).findall("Item"):
            service(cls).append(copy.deepcopy(c))

    starter_player = service("StarterPlayer")
    sps = new_item("StarterPlayerScripts", "StarterPlayerScripts")
    starter_player.append(sps)
    for c in child(kit, "StarterPlayer - StarterPlayerScripts").findall("Item"):
        sps.append(copy.deepcopy(c))

    # The kit has no ground or spawn point. Its hub floor is at y = 0, around the origin.
    ws = service("Workspace")
    ws.append(part("Part", "Baseplate", (0, -1, 0), (512, 2, 512), (99, 95, 98), material=512))
    ws.append(part("SpawnLocation", "SpawnLocation", (0, 0.5, 10), (6, 1, 6), (163, 162, 165)))

    shared = root.find("SharedStrings")
    if shared is not None:
        place.append(copy.deepcopy(shared))
    ET.ElementTree(place).write(out / "place.rbxlx", encoding="utf-8", xml_declaration=False)
    print("wrote", out / "kit.rbxmx", "and", out / "place.rbxlx")


if __name__ == "__main__":
    main()
