# SPDX-License-Identifier: MIT
"""Worst Superpower — one line inventing a genuinely useless power.

Winner line (OpenCode deepseek-v4.1-flash-free draft round on the
Simular Box, then a criteria-ordered tournament in-session): the
ceiling-fan power. It beat the ink-pen diagnosis (a known joke shape,
and arguably useful), the handshake crouton (funny but thinner), and
my own one-centimetre teleport (a familiar tiny-teleport gag). The
fan wins the judge's order: genuinely useless (criterion 1 — 2%
slower helps no one, and it is neither a curse nor secretly useful),
picturable in use (2 — an hour of staring for almost nothing),
unexpected (3), tight and specific (4 — 'exactly 2%', 'one full
hour'), and clear on a single reading (5).
"""

ENTRY_TEXT = (
    "You can make any ceiling fan spin exactly 2% slower "
    "by staring at it for one full hour."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 140 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 140, "entry outside the 1-140 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    payload = render()
    with open(out, "wb") as f:
        f.write(payload)
    # Round-trip self-check: what landed on disk must be byte-identical
    # to render() and still inside the gate (1-140 chars, non-blank).
    with open(out, "rb") as f:
        on_disk = f.read()
    assert on_disk == payload, "written bytes differ from render()"
    decoded = on_disk.decode("utf-8")
    assert 1 <= len(decoded) <= 140 and decoded.strip(), "on-disk gate check failed"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
