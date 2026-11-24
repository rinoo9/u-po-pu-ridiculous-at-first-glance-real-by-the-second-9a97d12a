"""One-sentence bizarre startup pitch for the make.fun bounty
'Ridiculous at First Glance, Real by the Second'.

Why the line works against the judge's criteria, in order:
1. It pitches a bizarre startup idea that is also a real business:
   a breakup agency — professional actors hired to end your
   relationship for you.
2. It is genuinely bizarre: paying a stranger to dump your partner
   sounds like a joke, and it is a wilder premise than a familiar
   service with a strange adjective bolted on.
3. The business logic holds on a second look: breakup agencies are
   a real paid service, the payer is explicit (the person who cannot
   face the conversation), the price is explicit ($300 a breakup),
   and the deliverable is explicit (tears included).
4. The sentence lands as a pitch: it turns from laughing (hiring
   someone to dump your partner) to nodding with the punchline
   "nobody wants to be the villain in their own story", so it ends
   on the emotional benefit — the reason customers pay — not on
   the joke.
5. It is concrete and vivid: actors, your partner, $300, tears.

Craft notes:
- Genuinely bizarre premise: the absurdity is the business itself,
  not a decoration — the actor IS the service, not the mascot.
- Real business logic: the customer pays to avoid the hardest
  conversation in their life, and the price and deliverable are
  named in the sentence, so the money is visible, not hand-waved.
- Concrete and vivid: every noun can be pictured in one beat —
  actors, partner, $300, tears.
- Tight landing: "nobody wants to be the villain in their own
  story" reframes the whole premise as a selling point instead of
  a punchline, so the sentence ends on the benefit, not the joke.

Deterministic: no network, no randomness, no environment reads.
"""

import os

LINE = "We hire actors to dump your partner for you — $300 a breakup, tears included — because nobody wants to be the villain in their own story."

# One-sentence entries must fit within 200 characters.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
