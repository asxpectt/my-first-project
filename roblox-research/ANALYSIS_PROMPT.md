# Prompt for analysing the downloaded transcripts

Paste this to Claude once `transcripts/` is filled (see `scripts/fetch_transcripts.py`):

> Read every file in `roblox-research/transcripts/`. For each topic folder
> (design, retention, loops, ui, monetization, fun):
> 1. List each video's 3–5 concrete techniques, with a number or example for each.
> 2. Merge the same advice when several videos give it, and count how many videos agree.
> 3. Flag advice that disagrees between videos.
> Then update `roblox-research/README.md`: replace any "from titles/descriptions only"
> notes with what the transcripts actually say, keep the "Apply to my game"
> checklist, and add techniques the search pass missed.
