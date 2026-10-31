# Dependencies and provenance

## Standalone installation

Install the complete `organize-chats` folder from a reviewed, immutable AI
Artifacts commit or its verified standalone ZIP into the runtime's configured
Agent Skills directory. Keep `SKILL.md`, this file, `LICENSE`, `references/`,
and `assets/` together. In Codex, the folder can be placed at
`.agents/skills/organize-chats` in a project. Start a fresh session, ask for a
chat audit, and confirm that the runtime actually discovers and invokes the
skill. Account access and supported operations must then be checked in that
runtime. The package itself does not grant chat permissions.

## Runtime requirements

The skill needs a runtime that discovers Agent Skills and can read this folder.
For direct chat changes, that runtime must expose authorized chat-management
tools for the recipient's own account. Supported browser control is optional.
With no direct tools, the user may supply an authorized transcript export or
inventory and receive an audit or manual organization plan. The package does
not provide account access, credentials, an MCP server, a background service,
or a schedule. It installs no software and requires no Python or Node runtime.

These instructions and fictional examples are Foculoom AI Artifacts source,
licensed under the [package-local Apache-2.0 license](LICENSE). Real chat
contents and migration records are consumer-owned inputs and must remain in
that consumer's authorized environment. No third-party code or data is bundled.
Record the installed revision and actual available tools when testing behavior;
package placement alone does not prove account compatibility.
