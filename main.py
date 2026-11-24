"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username -- one word, nothing else --
to entry.txt so the judge can compare it against other usernames.

Standard library only. No network calls.
"""

import os

USERNAME = "plm34554a"

# The gate accepts 1-30 characters of non-whitespace text; enforce it here
# so a typo in USERNAME can never produce an invalid entry.
assert 1 <= len(USERNAME) <= 30 and not any(ch.isspace() for ch in USERNAME), (
    "USERNAME must be a single word of 1-30 characters"
)


def output_path():
    """Resolve where the entry text goes.

    $MAKEFUN_OUTPUT wins when set; otherwise $MAKEFUN_OUTPUT_DIR/entry.txt;
    otherwise the default /output/entry.txt.
    """
    direct = os.environ.get("MAKEFUN_OUTPUT")
    if direct:
        return direct
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)


if __name__ == "__main__":
    main()
