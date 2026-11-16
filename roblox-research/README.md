# Roblox game research: design, retention, loops, UI, monetisation, fun

A study of the best tools for studying YouTube videos, the top Roblox development videos, and the techniques worth copying into our game. Researched 2026-11-16.

> **How this was made, and its limits.** YouTube is blocked in the cloud session that did this research, so nobody watched the videos or read their transcripts. The videos were found and summarised from search-engine indexes (titles, descriptions, chapter lists). They were then cross-checked against Roblox's official docs, the GameAnalytics 2026 benchmark report, Roblox DevForum posts and developer write-ups. Each technique below says where it came from. To upgrade this to a real transcript study, run `scripts/fetch_transcripts.py` on a PC, then use `ANALYSIS_PROMPT.md`.

---

## 1. Best GitHub repos for studying YouTube videos

Stars were checked on GitHub on 2026-11-16.

| Repo | Stars | Use it for |
|---|---|---|
| [jdepoix/youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) | 8.6k | **Best pick.** Gets the captions of any video as text, with no API key and no download. Our script uses it. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 208k | Downloads videos, audio, auto-captions and whole playlists or channels. Use it when a video has no captions (pair it with Whisper). |
| [jkawamoto/mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) | 498 | An MCP server, so Claude Code or Claude Desktop can pull transcripts itself. Actively maintained. |
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 607 | An alternative transcript MCP server. |
| [ZeroPointRepo/youtube-skills](https://github.com/ZeroPointRepo/youtube-skills) | 1.2k | Agent skills that get transcripts, search videos and browse channels. |
| [zarazhangrui/youtube-digest](https://github.com/zarazhangrui/youtube-digest) | 1.8k | Turns a video into study notes (transcript, summary, key points). |
| [nexmoe/VidBee](https://github.com/nexmoe/VidBee) | 11k | A desktop app that downloads, transcribes locally with speaker labels, and summarises. Good when you don't want to write code. |
| [jimmc414/onefilellm](https://github.com/jimmc414/onefilellm) | 2k | Packs transcripts, repos and papers into one text file for an LLM. |
| [Dicklesworthstone/bulk_transcribe_youtube_videos_from_playlist](https://github.com/Dicklesworthstone/bulk_transcribe_youtube_videos_from_playlist) | 0.7k | Transcribes a whole playlist with Whisper. |

**Recommended setup:** use `youtube-transcript-api` for batch work (this folder's script), add `mcp-youtube-transcript` so Claude can fetch one-off videos, and fall back to `yt-dlp` plus Whisper for videos without captions.

---

## 2. The videos

The full list of 42 videos, grouped by topic, is in [`videos.csv`](videos.csv). These are the top 20 on Roblox development and game design:

| # | Video | Why it's on the list |
|---|---|---|
| 1 | [The Retention Playbook: Turning Players into Fans](https://www.youtube.com/watch?v=YgyfcMfxQcI) | The creators of Jailbreak, Evade, Bee Swarm Simulator and Gunfight Arena on how they bring players back |
| 2 | [Core Loop Essentials](https://www.youtube.com/watch?v=bROouMt1b3g) | Roblox's own Game Insights designer explains the core loop |
| 3 | [Why 90% of Roblox Games Never Get Players](https://www.youtube.com/watch?v=xIBc5He_sy4) | Onboarding, retention benchmarks, monetisation |
| 4 | [How to Make Your Roblox Game BLOW UP](https://www.youtube.com/watch?v=SjSWCIGN5PM) | Chapters on ads, click-through rate, play rate, retention, visit length and monetisation, which is the algorithm funnel |
| 5 | [My Roblox Game Makes $12,535/mo (3K CCU)](https://www.youtube.com/watch?v=a170E9klbP4) | A real monetisation breakdown |
| 6 | [My Roblox Game Made $43,292](https://www.youtube.com/watch?v=-PoyiiGhoNo) | Which developer products sold best, and why |
| 7 | [Forsaken's ADDICTIVE Game Loop](https://www.youtube.com/watch?v=HqXmkkRvj0c) | Loop teardown of a game with 600M+ visits |
| 8 | [I made a dead game get 20 million visits](https://www.youtube.com/watch?v=JzB8fpyofnw) | Reviving a game that had died |
| 9 | [How I Made a FRONT PAGE Roblox Game](https://www.youtube.com/watch?v=nfuvVo-x740) | A front-page case study |
| 10 | [How to Make a Front Page Roblox Game](https://www.youtube.com/watch?v=AZTDrfuk9ME) | Front-page method |
| 11 | [Making a FRONT PAGE Roblox Game from Scratch](https://www.youtube.com/watch?v=PFY_CXf5zqw) | A one-day build challenge |
| 12 | [How To Make YOUR Roblox Game POPULAR](https://www.youtube.com/watch?v=fpDCkzz_HXQ) | Three growth strategies |
| 13 | [HOW TO MAKE A SUCCESSFUL ROBLOX GAME!](https://www.youtube.com/watch?v=qwHS1Q0i2Zc) | How to pick the idea |
| 14 | [Master Roblox Game Design: Ultimate Tips & Tricks](https://www.youtube.com/watch?v=_Fg45zCgDP8) | Immersive worlds, mechanics, polish |
| 15 | [Roblox Game Design for Beginners](https://www.youtube.com/watch?v=_USMDlml1HM) | A full design-to-publish run |
| 16 | [Can 14 Random Developers Make a Game in ONE Week?](https://www.youtube.com/watch?v=czFtDns-WRI) | BrawlDev's team-scoping lessons |
| 17 | [How to make a Roblox game (2025)](https://www.youtube.com/watch?v=QxAPBnXoK2U) | An up-to-date Studio workflow |
| 18 | [How To Make A Roblox Game: Complete Beginners Guide](https://www.youtube.com/watch?v=fIWEgoLb8dE) | Fundamentals |
| 19 | [core gameplay & networking, devlog #1](https://www.youtube.com/watch?v=3fDuCU1-5J4) | Building the loop and the netcode first |
| 20 | [Hotbar and Game Loop, Devlog #3](https://www.youtube.com/watch?v=JRfe4aPPfq0) | Building a core loop in Studio |

Channels worth following: **BrawlDev** (design theory, monetisation, analytics; 209k subscribers), **GnomeCode**, **AlvinBlox**, **TheDevKing**, and **Game Maker's Toolkit** for general design.

---

## 3. What the research says, by topic

### Player retention
- **Get players to the fun in under 5 minutes.** The core action should happen in under 10 seconds: in an obby, the player should be jumping within 10s. *(Roblox retention docs; Rolearn guide)*
- **Show, don't tell.** Use an arrow, an object they can interact with, and one satisfying feedback moment instead of text tutorials. Long tutorials lose players. One developer saw D1 go up after deleting their tutorial completely. *(Roblox engagement docs; Spaceport; TechCrunch)*
- **Give the first reward within 60 seconds.** *(dev guide; advice, not measured)*
- **Realistic benchmarks:** the median among games with 1M+ monthly players is **D1 10.3%, D7 1.6%, D30 0.5%**. A D1 under 25% after 60 days points to an onboarding problem. *(GameAnalytics 2026 report; Rolearn)*
- **For D1, track the onboarding funnel step by step and fix the step where players drop off most.** **For D7, add social features, new content and events.** *(retention video summary)*
- **Friends are the strongest retention lever.** A player with one real friend in the game stays far longer than a solo player. *(Rowatcher)*
- **Give players reasons to return:** daily rewards with a 7-day streak and a live countdown (Pet Simulator X, Adopt Me), regular updates with new cars, places and features (Jailbreak), and progress that keeps going while they're offline (Grow a Garden). *(daily-reward tutorials; DevForum "From the Devs")*
- **Pace progression.** If players progress too fast, they run out of content. *(Roblox docs)*

### Gameplay loops
- **Build the loop from four parts: action, reward, risk, progression.** The loop is the set of tasks the player repeats. *(Core Loop Essentials; loop primers)*
- **A simple, readable loop beats a deep one.** Grow a Garden's loop is plant → wait → harvest → sell → upgrade, with crops that grow while you're offline, so short check-ins pay off. Steal a Brainrot's loop is steal → run → stash → repeat, where risk and reward plus social pressure carry it. *(dev.to teardown; genre write-ups)*
- **Each reward should open up the next bigger goal**, for example: mine → craft better gear → reach deeper areas → better materials. *(loop video comments; Steal a Brainrot analysis)*
- **Asymmetric roles create replayability.** Forsaken pits one killer against everyone else. *(Forsaken summary)*
- **Aim for sessions of 19 minutes or more.** Games with 0–6 minute sessions struggle to survive, though a long session alone doesn't make players spend. *(GameAnalytics / InvestGame)*

### The new UI design (2026)
- **Roblox UI Styling came out of beta in January 2026.** You write StyleRules and StyleSheets once, with design tokens and themes such as light and dark, and edit them in the Style Editor instead of setting colours on every element. *(DevForum announcement; creator-docs)*
- **StyleQuery (May 2026)** applies rules based on an element's size or aspect ratio, so one layout adapts to phone, tablet and PC. *(DevForum)*
- **Styling Transitions (July 2026)** let a StyleSheet tween hover and press effects with no code. *(DevForum)*
- **The current look:** a chunky, layered "simulator" style built from duplicated, darkened shapes for depth, plus gradients, UIStroke outlines and shine highlights. *(Stud-UI kit; Figma-to-Studio guide)*
- **HUD layout:** put action buttons (Shop, Pets, Rebirth) on a bottom or side rail, keep everything inside the safe area, and test at phone size first. *(simulator HUD guides)*
- **Shop layout:** a header with the shop's name, the player's balance and a close button, with **at most one featured offer** so the screen stays clean. *(shop GUI guides)*
- **Technical tips:** use UIAspectRatioConstraint and Scale sizing instead of Offset, UICorner progress bars, and UIPageLayout for tabs. *(Essential UI Tips & Tricks)*

### Monetisation
- **Game passes are one-time and permanent; developer products can be bought again and again.** Use passes for permanent perks (VIP, 2x, extra slots) and products for consumables (currency packs, boosts, revives, skips). *(Roblox docs)*
- **Roblox keeps 30%**, so a 100 Robux sale pays you 70 Robux, about 27 cents through DevEx. Set prices with that in mind. *(several sources)*
- **Developer products often earn the most in big games** because loyal players keep buying them. A blog's rule of thumb is 60–70% of your shop items as passes and 30–40% as products. *(secondary; unverified)*
- **Use Roblox's price optimisation tool** instead of guessing prices, and read per-product sales in Creator Hub analytics to see what sells. *(Roblox docs; DevForum)*
- **Don't fake scarcity**, such as claiming a limited time or limited stock that isn't real. Use PolicyService to hide paid random items in regions that restrict them. Process receipts properly. *(Roblox docs)*
- **Since 29–30 May 2026, developer products and passes can't be sold across games.** Each one sells only inside its own game. *(Roblox docs)*
- **Engagement payouts:** Creator Rewards pays for time played and return visits, and rewarded video ads were expanded at RDC 2025. Retention now earns money directly. *(RDC 2025 newsroom)*
- **Avoid pay-to-win.** Sell speed, convenience and looks, and state the benefit clearly on the button. *(several guides)*

### What makes a game fun
- **Juice:** screen shake, particles, sound, squash and stretch, and number pop-ups make the same rules feel far better. *("Juice it or lose it", 2012; "The art of screenshake")*
- **Game feel:** respond to input instantly and make every action read clearly. *(Steve Swink; Cornell game-feel course)*
- **Impact:** players love seeing the world change because of them. *(DevForum "Game Design 101")*
- **Controlled randomness:** give a chance, not a guarantee. Repeated actions with no impact are boring. *(DevForum "What makes a game fun")*
- **Pacing:** alternate tension and release, and raise the challenge as skill grows. *(DevForum "Game Design 101")*
- **Mastery and expression:** a skill ceiling to climb plus things to show off (skins, titles, leaderboards).

---

## 4. The best techniques, ranked by impact per hour of work

1. **Reach the core action within 10 seconds and the first reward within 60 seconds**, with no text tutorial and an arrow instead. This is the biggest D1 lever.
2. **A loop players can read in one sentence**, where each reward opens a bigger goal, plus offline progress so short return visits pay off.
3. **Juice every core action** with a sound, a particle effect and a number pop-up. It's cheap and changes how the game feels.
4. **Daily reward with a 7-day streak and a countdown**, plus a weekly update or event. This is the D7 lever.
5. **Make friends matter:** an invite reward, a co-op bonus, trading or gifting. This is the strongest retention lever.
6. **A clean, UI Styling-based HUD and shop**: one theme, phone-first, one featured offer.
7. **A small, fair shop:** 3–5 passes (VIP, 2x currency, extra slot, auto-collect) and 3–5 products (currency packs, boost, skip), with prices set by the price optimisation tool.
8. **Analytics from day one:** funnel events for each onboarding step, and checks of D1, D7 and session length against the benchmarks above.

## 5. Apply it to our game: checklist

The repo has no Roblox game in it yet, so these are steps for the design doc (`design.md`). Fill in the blanks once the genre is chosen.

- [ ] **Loop sentence:** "Players ___ to earn ___, spend it on ___ so they can ___ faster/further." Keep it under 15 words.
- [ ] **First 60 seconds, scripted beat by beat:** spawn → arrow → first action within 10s → reward pop-up with juice → first upgrade bought by 60s.
- [ ] **Session target of 20+ minutes:** at least 3 tiers of goals (a 2-minute goal, a 10-minute goal, a session goal).
- [ ] **Return hooks:** offline progress, a daily streak, and a weekly event on a fixed day.
- [ ] **Social:** a friend-join bonus (for example +10% earnings per friend in the server), gifting or trading, a leaderboard.
- [ ] **UI:** one StyleSheet with tokens; HUD rail and shop built with the `roblox-ui` skill and checked at 4 screen sizes.
- [ ] **Monetisation table:** passes and products with prices, each with its benefit in one line. No pay-to-win.
- [ ] **Funnel analytics:** an AnalyticsService funnel event for each onboarding step.
- [ ] **Juice list:** a sound, a particle effect and a camera or number effect for each core action (`roblox-sound`, `roblox-vfx`).

## Sources (non-video)
- Roblox Creator Hub: [retention](https://create.roblox.com/docs/production/analytics/retention), [engagement](https://create.roblox.com/docs/production/analytics/engagement), [monetisation](https://create.roblox.com/docs/production/monetization), [developer products](https://create.roblox.com/docs/production/monetization/developer-products), [UI styling](https://github.com/Roblox/creator-docs/blob/main/content/en-us/ui/styling/index.md)
- DevForum: [UI Styling full release](https://devforum.roblox.com/t/full-release-ui-styling-is-officially-released/4275082), [StyleQuery](https://devforum.roblox.com/t/full-release-stylequery-more-styling-features/4566519), [Styling Transitions](https://devforum.roblox.com/t/full-release-styling-transitions/4646870), [What makes a game fun?](https://devforum.roblox.com/t/what-makes-a-game-fun/1845475), [Game Design 101](https://devforum.roblox.com/t/game-design-101-how-to-make-your-game-fun-enjoyable-and-replayable/1886641)
- [GameAnalytics 2026 Roblox Benchmark Report](https://www.gameanalytics.com/reports/2026-roblox-report), [2025 report](https://www.gameanalytics.com/reports/2025-roblox-report)
- [RDC 2025 newsroom](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025)
- [Medium "From the Devs": first impressions](https://medium.com/roblox-developer/from-the-devs-the-importance-of-first-impressions-on-player-retention-by-silky-dev-e63a90291279), [Medium "From the Devs": making your game last](https://medium.com/roblox-developer/from-the-devs-making-your-game-last-a-quick-guide-on-player-retention-by-nurgenius-df31dab6b0fa)
- [Rolearn first-week retention](https://rolearn.dev/guidance/first-week-retention-optimization/), [Spaceport: hook players in 2 minutes](https://www.spaceport.xyz/blog/how-to-hook-players-in-the-first-2-minutes-game-retention-tips-for-roblox-devs), [dev.to Grow a Garden / Steal a Brainrot loop](https://dev.to/wlz/why-grow-a-garden-and-steal-a-brainrot-bet-on-boring-idle-tech-the-luau-loop-behind-2djf), [Stud-UI kit](https://github.com/TemporaryLooker22/Stud-UI-Clean-Roblox), [Rolearn game-pass pricing](https://rolearn.dev/guidance/roblox-gamepass-pricing-strategy-guide/)

## Log
- 2026-11-16: First research pass done through search indexes, because YouTube was blocked. Added the video list, the transcript fetcher and the analysis prompt.
