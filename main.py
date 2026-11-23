"""Entry for make.fun's "One Emoji, One Smile" bounty.

Writes exactly one emoji to entry.txt in the output directory:
UTF-8 text of 1 to 8 characters, nothing else. The same bytes
are written on every run.
"""

import os

# Draft: smiling face with smiling eyes (U+1F60A) — warm, but the
# first smiley anyone reaches for; the judge brief rewards a face
# that feels chosen rather than default.
# Revised: hugging face (U+1F917) — open hands and a grin read as
# kind and gently funny at first glance, universal across ages,
# and safe from a stranger: friendly without intimacy or flirtation.
EMOJI = "\U0001F917"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(EMOJI.encode("utf-8"))


if __name__ == "__main__":
    main()
