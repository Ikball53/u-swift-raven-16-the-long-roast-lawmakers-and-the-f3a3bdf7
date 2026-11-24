"""Write the competition entry line to /output/entry.txt.

The entry is one satirical sentence, and the file must hold exactly that
sentence with no trailing newline, so the gate counts its characters only.
"""

from pathlib import Path

ENTRY_LINE = "The senator who wrote 214 pages of rules for artificial intelligence spent 40 minutes failing to save the bill as a PDF, then faxed it to himself instead."

TARGET = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts 1 to 320 characters; refuse loudly rather than
    # silently submitting an entry the judge would never see.
    if not 1 <= len(ENTRY_LINE) <= 320:
        raise ValueError(f"entry is {len(ENTRY_LINE)} characters, must be 1-320")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(ENTRY_LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
