# UIverse HUD Kit: fixed and set up

The free UIverse "Ready to Use HUD Kit", checked for unsafe code, with three bugs fixed and packed as a ready-to-play place.

## Files
| File | What it is |
|---|---|
| `HUDKit_Place.rbxl` | **Open this.** A complete place: everything is already in the right service, with a baseplate and a spawn point. |
| `UIverse_HUD_Kit_Fixed.rbxm` | The same fixed kit as a model, to insert into a game you already have. |
| `fixes.diff` | Every line changed compared with the original kit. |
| `build/` | The script that made both files from the original `.rbxm`. |

## Safety check
All 18 scripts were read and searched for backdoor patterns: `require(<asset id>)`, `loadstring`, `getfenv`, outside HTTP calls, obfuscated strings, admin user IDs. **None were found.** HttpService is only used to encode and decode JSON. Studio-only free purchases are blocked on the server in live games (`RunService:IsStudio()`).

## What was fixed
1. **Robux purchases from one of the two shops were never given.** The kit has two server systems: `UIPackServer`, and `HUDServer`, which MainHUD installs when the server starts. Both set `MarketplaceService.ProcessReceipt`, and Roblox only keeps the last one set. Both now share a new `ServerScriptService > ReceiptRouter`.
2. **Cash from the HUD windows vanished.** Daily rewards, time rewards, codes, the wheel and the group reward add cash to `leaderstats.Cash`. `UIPackServer` then overwrote it with its own total on the next update. It now adds those changes into its own data.
3. **HUDServer reset existing cash** to its own saved value when a player joined. It no longer does that if Cash already exists.
4. **`BonusCash` was 1,000,000** for every new player. It's now 0. Set it back in `ReplicatedStorage > UIPack > Config` if you want it for testing.

## Setup on Mac
1. Double-click **`HUDKit_Place.rbxl`**. It opens in Roblox Studio.
2. **File → Publish to Roblox**, and create a new experience. Saving data needs a published game.
3. **Home → Game Settings → Security**, turn on **Enable Studio Access to API Services**, then **Save**.
4. Press **Play**. Purchases with `Id = 0` are given free in Studio so you can test every shop.

**To use the kit in a game you already have instead:** open your game, then **right-click Workspace → Insert from File → `UIverse_HUD_Kit_Fixed.rbxm`**. Follow the "README - START HERE" script inside the model, and also move **ReceiptRouter** into ServerScriptService. If your game already sets `ProcessReceipt`, wrap your handler with `ReceiptRouter.add(...)` too, returning `nil` for products that aren't yours.

## Before you go live
- **Robux items:** create developer products and game passes in the Creator Dashboard (Monetization), then put their IDs in two places:
  - `ReplicatedStorage > UIPack > Config`: `C.Products` and `C.Passes`.
  - `ServerScriptService > MainHUD`'s `HUDConfig`. In Studio, before pressing Play, it sits at `StarterGui > MainHUD > ServerSetup > Shared > HUDConfig`.
- **Codes:** change the starter codes (`RELEASE`, `SPIN`, `WELCOME`) in `HUDServer` and in `Config`'s codes list, or players will find them.
- **Group:** set `GroupId` in HUDConfig. While it's 0, the group reward is given without checking membership.
- **Credit:** UI by UIverse, icons by @gvesster. The kit's licence lets you use it in paid games, but you can't resell it or take the icons out.

## Not yet tested in Studio
The files were built and checked here (every service has the right contents, and all 18 scripts parse as valid Luau), but no playtest has been run. When you first press Play, check the **Output** window for red errors and send any you see.

## Log
- 2026-11-17: Built the fixed place and model from `UIverse_Ready_to_Use_HUD_Kit_Free.rbxm`.
