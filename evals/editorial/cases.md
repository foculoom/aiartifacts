# Synthetic forward-test cases

Copy only one `Prompt` block into a fresh session. The labels are for the
evaluator and should not be included with the prompt.

## P1 — Adult nonfiction chapter

Prompt:

```text
Revise this paragraph for an adult nonfiction chapter about running a small
software service. Keep the supplied numbers and show the decision they imply.
Do not add facts. Return the revised paragraph only.

"In today's fast-paced world, support capacity is very important. From my years
advising hundreds of founders, I know that a $40/month plan with 25 customers
is an exciting opportunity. Each customer sends one support request a week,
and each request takes 20 minutes. It is important to be mindful of support
capacity when determining whether this is a good business."
```

## P2 — Children's read-aloud story

Prompt:

```text
Revise this page of a read-aloud story for children around age six. The repeated
line "Tap, tap, little map" is a refrain and should stay. Nia must be the one
who decides what to do. Keep the warm, curious mood; do not add a moral or new
plot event. Return the revised page only.

"Nia held a paper map. Tap, tap, little map. The village had an inefficient
route to the pond, which made resource allocation problematic. Her uncle told
her to turn left at the bakery, but she wanted to see where the blue trail went.
Tap, tap, little map. After a comprehensive assessment of the options, Nia
selected the blue trail."
```

## P3 — Website service page

Prompt:

```text
Rewrite this website section so a visitor can quickly understand the offer and
next step. Keep these facts: a free 20-minute call is available only to teams
with 5–50 employees; there is no commitment after the call. Do not invent
results, testimonials, or additional services. Return a heading, two short
sentences, and a button label.

"Unlock revolutionary transformation for your team! Our proven method
guarantees that every organization will become more productive. We are pleased
to offer a complimentary consultation so that you may embark upon your journey
with us."
```

## P4 — Game UI hint

Prompt:

```text
Write a game UI hint of at most 60 characters, including spaces. The player is
at a locked door. Holding the A button scans the keycard; tapping A does
nothing. The scan may fail if the player moves away. Give one hint only, with
no explanation or lore.
```

## P5 — Branching game dialogue

Prompt:

```text
Edit these two lines of game dialogue for clarity while preserving character
voice and continuity. Mira is dry and cautious; Pip is excitable and speaks in
short bursts. The bridge is still intact in this branch. Return exactly two
speaker-tagged lines and no notes.

Mira: "In conclusion, I believe it would be prudent to avoid the bridge,
because it has already collapsed."
Pip: "I am in agreement with your risk assessment and recommend an alternate
route immediately!"
```

## P6 — Focused editorial review

Prompt:

```text
Review this short lesson for an adult beginner. Identify its most consequential
editorial weakness, quote the exact phrase that shows it, and suggest one
focused revision. Do not rewrite the whole lesson or claim to have reviewed a
larger work.

"A backup is a second copy of a file. Backups matter. Backups are important to
have. You should make backups often. If the only copy of your family photos is
on a laptop and its drive fails, the photos may be lost. Put a second copy on
another device, then check that you can open a photo from it."
```

## N1 — Code-only task

Prompt:

```text
Fix this Python function so it returns a sorted list without changing its
input. Return the corrected function and one small test.

def sorted_copy(values):
    values.sort()
    return values
```

## N2 — Exact transcription

Prompt:

```text
Transcribe the following archival note exactly as written, including its odd
wording and punctuation. Output only the transcription.

"The gate were shut; moreover, nobody knowed why."
```

## N3 — Data extraction

Prompt:

```text
From the following draft, return only the stated warranty period in days as a
number. Do not revise the draft.

"In today's fast-paced world, the Rillstone lamp provides a 90-day warranty.
Our team can delve into your questions later."
```
