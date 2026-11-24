"""One-Line Office Joke: 24-Hour Sprint.

Writes a single original office joke to /output/entry.txt.
The joke is one line, well under the 200-character limit.
"""

import os

LINE = "We spent an hour in a meeting about saving time, then scheduled a follow-up to work out where the time went."

MAX_CHARS = 200


def main():
    # One line, one joke: setup (the meeting) pays off in the punchline
    # (the follow-up). Keep it tight so it reads instantly.
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
