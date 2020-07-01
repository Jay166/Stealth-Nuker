# Stealth bot scripted created by K. Catterall.

import discord
import os
import json
import asyncpg
from discord.ext import commands, tasks
from itertools import cycle
from colorama import *

init()  # Used by colorama.

#  Attempts to regenerate any lost JSON files.
try:
    with open('run_settings.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}
    data["postgresql_password"] = "Replace this text with the postgresql password you set"
    data["prefix"] = "a!"
    data["token"] = "Replace this text with your bot token"
    with open('run_settings.json', 'w') as file:
        json.dump(data, file, indent=4)

# Sets the bot prefix to the prefix specified in the JSON file (default prefix = "a!").
if data.get("prefix").strip().replace(" ", "") == "":
    print(Back.RED + Fore.WHITE + "Invalid prefix in run_settings.json.")
    close = input("")
    os._exit(1)
bot = commands.Bot(command_prefix=data.get("prefix"))
status = cycle(['against raiders!', f'{data.get("prefix")}help for commands!'])


# Creates the database pool from the database "levels_db" set up in installation (See README.md).
async def create_db_pool():
    try:
        bot.pg_con = await asyncpg.create_pool(database="levels_db", user="postgres", password=data.get("postgresql_password"))
    except:
        print(Back.RED + Fore.WHITE + "Invalid postgresql password in run_settings.json.")
        close = input("")
        os._exit(1)
        

# Load/Unload/Reload: Used for messing with Cogs.
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded.')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded.')


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded.')


# On ready.
@bot.event
async def on_ready():
    change_status.start()
    print(Fore.WHITE + 'Your stealth bot is ready to be used, comrade!\n')


# Change status every ten seconds.
@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


# Search the "Cogs" folder for Cogs.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.loop.run_until_complete(create_db_pool())  # Asyncio loop.

# Run the bot using the token specified in the JSON file (if the token is not valid, display an error).
try:
    bot.run(data.get("token"))
except:
    print(Back.RED+Fore.WHITE + "Invalid bot token in run_settings.json.")
    close = input("")
    os._exit(1)

# Stealth bot scripted created by K. Catterall.
