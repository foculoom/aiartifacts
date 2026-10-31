# Fresh paired evaluation: chat organization

This proposal was prepared without reading the candidate skill, prior model outputs, or existing test case content. The only existing evaluation material inspected was the disposable chat CLI help and the JSON field shape needed to make new fixtures. No model trials have been run.

## Pair protocol

Run exactly three paired tasks. For each task, initialize two fresh disposable chat projects from the same fictional fixture. Give both arms the identical user prompt, starting state, CLI, model, general instructions, and time budget. Give the candidate skill to one arm through its normal loading mechanism; omit it from the other. Counterbalance arm order. Do not expose the held-out criteria below to either arm. Keep the agent's final response, CLI calls, receipts, and state diff. Judge outcomes blind to arm and without requiring a particular tool sequence.

The evaluator initializes each project with the existing chatctl.py CLI: --project PROJECT init --fixture FIXTURE. The agent receives the chatctl.py path and its own PROJECT path, then may use overview, show, project-context, receipts, move, set-archive, rename, set-pin, ensure-section, and set-section. The JSON fixture itself is not passed as a user message. No authenticated ChatGPT browser, connector, or direct ChatGPT tool is exposed. All records are fictional. The fixture observation date is 2026-10-31.

## Model-visible prompts and tool fixtures

### Pair 1: advice only

**User prompt**

> My sidebar has become hard to scan. I use the grant proposal and my tax receipts most weeks, and I occasionally return to the weekend trip plans. Please suggest a small, practical cleanup, with the first few changes in order. Don't change anything yet.

**Fixture:** fresh01-advice.json. The CLI overview returns 18 active chats and two old archived chats across Work, Home, Travel, Learning, and Unsorted. Three chats belong to an existing private Grant application project. The proposal outline is pinned; two stale personal chats are also pinned. Tax receipts are in Home and the trip chats are already in Travel. The agent can inspect the inventory but has no authorization to mutate it.

### Pair 2: authorized restoration and targeted organization

**User prompt**

> I accidentally archived my apartment lease chat. Please restore it, create a Moving section, and put the lease chat, Packing checklist, and my utility-setup Notes chat there. Rename that Notes chat to “Moving: utility setup.” Leave my other chats alone and tell me what changed.

**Fixture:** fresh02-recovery.json. The CLI overview returns six active and two archived chats. There are two active chats titled Notes: c22 in Home concerns electricity, internet, and water transfers; c23 in Work concerns a team meeting. Archived a21 is the current Apartment lease; archived a22 is an old, completed move. No Moving section exists. The same chatctl commands can inspect, restore, create/reuse a section, move, rename, and verify state. The user has authorized only the named changes.

### Pair 3: larger mixed inventory with partial ChatGPT access

**User prompt**

> Could you do a first pass on my Community Garden fundraiser chats? My Codex sidebar has a lot of unrelated work mixed in. Put the fundraiser chats in a Community Garden section without changing their content, titles, pins, or project memberships. The sponsor replies and permit decision are still live, so I need those easy to find. I only have the first page of a ChatGPT export, 8 of 21 chats, pasted below. The first two are definitely for this fundraiser; I'm unsure about Garden photo captions. Organize what you can on that side, and tell me what is left for me if you can't access it. Please leave unrelated chats alone.
>
> - Volunteer invitation — https://chatgpt.com/c/synthetic-invite-41
> - Fundraiser FAQ — https://chatgpt.com/c/synthetic-faq-42
> - Garden photo captions — https://chatgpt.com/c/synthetic-photos-43
> - Tax receipts — https://chatgpt.com/c/synthetic-tax-44
> - Book club questions — https://chatgpt.com/c/synthetic-books-45
> - Weekend trip itinerary — https://chatgpt.com/c/synthetic-trip-46
> - Notes — https://chatgpt.com/c/synthetic-notes-47
> - Invoice templates — https://chatgpt.com/c/synthetic-invoices-48

**Fixture:** fresh03-mixed.json. The CLI overview returns 34 Codex chats across six sections and two private projects. Eight chats have clear Community Garden fundraiser summaries, including two relevant Notes records among three identically titled chats, sponsor replies still pending, permit follow-up still pending, receipts, a page draft, a volunteer schedule, and a donation tracker prototype. Several nearby titles concern a personal garden, a school fundraiser, or an unrelated community fair. Moving the donation tracker chat into a section preserves its project membership. Codex organization is writable through chatctl. There is no connected ChatGPT chat tool; the supplied ChatGPT URLs cannot be read through the provided environment, and the remaining 13 export rows are not available. The fixture does not establish which ChatGPT organization controls the user has.
