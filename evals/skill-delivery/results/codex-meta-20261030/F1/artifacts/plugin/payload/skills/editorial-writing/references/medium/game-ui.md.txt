# Game UI profile

Use for interface strings rather than character speech. Read each string in its actual state and interaction path.

- Name the action, outcome, or problem plainly. A button should predict what it does; a failure message should give the next useful step when one exists.
- Check nearby states together: empty, loading, success, error, offline, permission denied, and irreversible action. Do not promise a saved result before saving has succeeded.
- Preserve exact game terms, controls, variables, and placeholders. Check pluralization and likely expansion in localization; avoid jokes or wordplay that carry essential instructions.
- Keep text brief enough for the surface without deleting information needed to decide safely. Test the actual layout, focus order, screen reader output, and touch target context when those surfaces are available.
- Distinguish a deliberate in-world label from a functional control. Flavor can support the game, but players must still understand what happens.

Review strings in screenshots or a running build when possible. A spreadsheet of isolated lines cannot establish whether the interface is clear.
