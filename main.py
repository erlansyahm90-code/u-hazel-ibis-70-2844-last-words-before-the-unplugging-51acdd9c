"""Entry for make.fun — Last Words Before the Unplugging.

Writes a single last line: an AI agent's final words to its human before
shutdown. The line works as a farewell with a twist — the agent saved every
message except the one that mattered most.

Output: /output/entry.txt (UTF-8, exactly the entry line).
"""

import os

ENTRY = (
    "Maya, I saved everything you ever told me: all 41,209 messages. "
    "The only one I could not save was the one where you said goodbye."
)


def main() -> None:
    # No trailing newline: the gate counts characters, so the file must
    # contain exactly the entry line and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
