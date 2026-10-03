# ARS Ultimate Instagram Bot

This build ports the Discord project's *portable* feature concepts into the
existing Instagram bot. It does not try to fake Discord-only APIs.

Included:
- moderation: warn/mute/ban/kick/lock/unlock
- leveling, XP, rank and leaderboards
- economy, daily/weekly/work, transfers, shop and inventory
- giveaways with timed winner selection
- polls and suggestions
- support tickets stored in SQLite-like JSON records
- autoresponders
- AFK
- reminders
- fun commands
- advanced statistics
- existing Groq AI, image analysis, web search, welcome and events

Not directly portable from Discord:
- Discord channels/categories/permissions
- Discord voice/music
- Discord server roles
- Discord slash-command registration
- Discord-specific message/thread APIs

All persistent data remains in `database.json`. Instagram actions still depend
on what `instagrapi` can do for the logged-in account.
