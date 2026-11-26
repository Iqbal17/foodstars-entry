"""One Star, Five Stars for the Food (u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

Entry: one sentence, at most 200 characters, in the voice of an alien
tourist giving planet Earth a one-star review while still slipping in a
real compliment about the food. Gate: /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space, a single line.

Candidates weighed (both the one-star complaint AND the food compliment
must land, in a convincingly alien voice, funniest first):
A - "One star: the gravity is rude, the weather leaks, and the locals
scream at glowing rectangles, but the cheese here almost justifies the
trip." LOSES: "almost justifies" is a shrug of a compliment, and cheese
is the most expected Earth food.
B - "Terrible planet, would not orbit again: it rained on my antenna and
charged me for parking my saucer, though the dumplings were very good."
CLOSE: complaint and compliment both land, but "very good" is flat.
C - "One star for making me breathe your soup-thick air and queue to
leave, five stars for the warm bread discs you call pancakes." LOSES:
two star ratings fight each other; the brief wants one star overall.
WINNER v1 - "One star: your planet charges rent for gravity, rains
without asking, and made me queue to leave, but the noodles were worth
the trip."

Writing passes on the winner:
Pass 1 (v1 above) tested at 134 chars, gate-clean: the one-star frame,
three complaints and the noodle compliment all land. But the compliment
is weak tea - "worth the trip" is what a polite human tourist writes,
and the alien never sounds like leaving was ever in doubt.
Pass 2 (final) - "One star: your planet charges rent for gravity, rains
without asking, and made me queue three hours to leave - but I would
cross six galaxies again for your noodles." Two upgrades: "queue three
hours to leave" gives the complaint a specific, petty, review-writer
detail (real one-star reviews always time the queue), and "cross six
galaxies again" makes the compliment cost the alien something enormous,
which is exactly why it reads as genuine instead of slipped-in. The
one-star verdict never wavers, as the brief demands.

Revision note - why the gate guard rejects embedded newlines: the brief
asks for one sentence on a single line, and a newline inside the text
would make entry.txt hold two lines even though the character count
still passes. The count check alone cannot catch that, so check_gate
rejects "\\n" explicitly; the trailing newline main() appends is the
file terminator, not part of the entry.
"""

import os

# Winner: the complaint stays petty and specific (a timed queue), the
# compliment costs six galaxies - so both halves read as sincere.
ENTRY = "One star: your planet charges rent for gravity, rains without asking, and made me queue three hours to leave - but I would cross six galaxies again for your noodles."
MAX_CHARS = 200


def describe_gate():
    """Return the sealed gate as one human-readable description."""
    return "1-%d UTF-8 characters, not only white space, single line" % MAX_CHARS


def check_gate(text):
    """Mirror the sealed gate: 1-200 UTF-8 chars, not only white space."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must satisfy the gate (%s), got %d chars"
                         % (describe_gate(), len(text)))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def validate_entry(text):
    """Validate an entry against the gate, with one clear error message."""
    try:
        check_gate(text)
    except ValueError as exc:
        raise ValueError("invalid entry %r: %s" % (text, exc)) from exc
    return text


def entry_path():
    """Write under $MAKEFUN_OUTPUT_DIR, falling back to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
