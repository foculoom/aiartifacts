# Chat Organizer

The [organize-chats skill](skills/organize-chats/SKILL.md) reviews accessible
conversations, proposes durable work areas, and applies changes the user has
authorized when their host exposes the required tools. It works with supplied
inventories or authorized exports when direct chat access is unavailable.

## Install a reviewed revision

Choose an immutable reviewed commit. Plugin-capable clients install
`plugins/chat-organizer`; standalone skill installers use
`plugins/chat-organizer/skills/organize-chats` from the same revision. The AI
Artifacts marketplace catalog makes the plugin available to compatible desktop
clients. Client installation commands and supported chat tools vary; verify the
installed file inventory and test the actual runtime before claiming support.
Installing the skill does not grant access to chats or change account settings.

The package has no MCP server or hosted service. See the
[skill dependencies](skills/organize-chats/DEPENDENCIES.md) and the
[package license](LICENSE). Its synthetic evaluations remain outside the
installable package. A source commit, installed package, public listing, and
successful organization of a recipient's account are separate results.
