# Stealth bot scripted created by K. Catterall.

import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
from colorama import *

init()  # Used by colorama.

#  Attempts to regenerate any lost JSON files.
try:
    with open('token.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}
    data["token"] = "Replace this text with your bot token"
    data["prefix"] = "a!"
    with open('token.json', 'w') as file:
        json.dump(data, file, indent=4)

# Sets the bot prefix to the prefix specified in the JSON file (default prefix = "a!").
client = commands.Bot(command_prefix=data.get("prefix"))
status = cycle(['against raiders!', f'{data.get("prefix")}help for commands!'])


# Load/Unload/Reload: Used for messing with Cogs.
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded.')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded.')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded.')


# On ready.
@client.event
async def on_ready():
    change_status.start()
    print(Fore.WHITE + 'Your stealth bot is ready to be used, comrade!\n')


# Change status every ten seconds.
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# Search the "Cogs" folder for Cogs.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# Run the bot using the token specified in the JSON file (if the token is not valid, display an error).
try:
    client.run(data.get("token"))
except:
    print(Back.RED+Fore.WHITE + "Incorrect token: Please check token.json and add the correct bot token.")
    close = input("")
    os._exit(1)

# Stealth bot scripted created by K. Catterall.
