"""Download transcripts for every video in videos.csv.

Usage (needs youtube.com reachable, e.g. on your own PC):
    pip install youtube-transcript-api
    python scripts/fetch_transcripts.py            # all topics
    python scripts/fetch_transcripts.py ui fun     # only some topics

Writes transcripts/<topic>/<video_id>.txt. Already-downloaded files are skipped,
so you can re-run it after a failure. Then ask Claude to read the folder with
the prompt in ANALYSIS_PROMPT.md.
"""

import csv
import sys
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    wanted = set(sys.argv[1:])
    api = YouTubeTranscriptApi()
    ok = failed = 0
    with open(ROOT / "videos.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if wanted and row["topic"] not in wanted:
                continue
            out = ROOT / "transcripts" / row["topic"] / f"{row['video_id']}.txt"
            if out.exists():
                continue
            try:
                fetched = api.fetch(row["video_id"], languages=["en", "en-US", "en-GB"])
            except Exception as e:  # no captions, private video, rate limit...
                print(f"FAIL {row['video_id']} {row['title']}: {type(e).__name__}")
                failed += 1
                continue
            text = " ".join(s.text.replace("\n", " ") for s in fetched)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(
                f"# {row['title']}\nhttps://www.youtube.com/watch?v={row['video_id']}\n\n{text}\n",
                encoding="utf-8",
            )
            print(f"OK   {row['video_id']} {row['title']}")
            ok += 1
            time.sleep(1.5)  # be gentle; YouTube rate-limits fast scrapers
    print(f"\n{ok} downloaded, {failed} failed")


if __name__ == "__main__":
    main()
