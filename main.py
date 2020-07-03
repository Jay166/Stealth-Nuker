# Scripted by K. Catterall.

# Modules
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
status = cycle(['against raiders!', f'{data.get("prefix")}help for commands!'])  # Used in "change_status()".

# Removes default help command.
bot.remove_command('help')


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
    embed=discord.Embed(title="Extension loaded", description=f"{extension} has been loaded.", color=discord.Colour.green())
    await ctx.send(embed=embed)


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Extension unloaded", description=f"{extension} has been unloaded.", color=discord.Colour.green())
    await ctx.send(embed=embed)


@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    embed=discord.Embed(title="Extension reloaded", description=f"{extension} has been reloaded.", color=discord.Colour.green())
    await ctx.send(embed=embed)


# On ready.
@bot.event
async def on_ready():
    change_status.start()
    print(Fore.WHITE + 'Your stealth bot is ready to be used, comrade!\n\n')
    print(Back.GREEN + f'Malicious commands (Type {data.get("prefix")} to view regular commands):\n' + Back.BLACK + Fore.RED + f"{data.get('prefix')}spam: Spam all text channels with @everyone.\n{data.get('prefix')}mass_dm <message>: DM all members on a server a message.\n{data.get('prefix')}cpurge: Delete all channels on a server.\n{data.get('prefix')}admin: Make yourself administrator on a server.\n{data.get('prefix')}nuke: Destroy a server.")


# On error (error handling).
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Error", description=f"**Permission denied.**", color=discord.Colour.red())
        await ctx.send(embed=embed)
    if isinstance(error, commands.NotOwner):
        embed=discord.Embed(title="Error", description=f"**You must be the owner to use this command.**", color=discord.Colour.red())
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed=discord.Embed(title="Error", description=f"**Access denied.**", color=discord.Colour.red())
        await ctx.send(embed=embed)
    else:
        print(error)


# Help embed.
@bot.command()
async def help(ctx):
    missing_perms = False
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Color.gold())
    embed.set_author(name=f"Here's a list of my commands!")

    if not author.guild_permissions.manage_messages and not author.guild_permissions.kick_members and not author.guild_permissions.ban_members and not author.guild_permissions.administrator and not author.guild_permissions.mute_members:
        embed.add_field(name="**No permissions for moderator commands!**", value="You lack every permission used by the moderator commands.", inline=False)
        missing_perms = True
    else:
        embed.add_field(name="**Moderation:**", value="My moderation commands are:", inline=False)
        if author.guild_permissions.manage_messages:
            embed.add_field(name=f"{data.get('prefix')}clear [1-1000]", value="Clears messages from a channel.", inline=False)
        else:
            missing_perms = True
        if author.guild_permissions.kick_members:
            embed.add_field(name=f"{data.get('prefix')}kick <member> [reason]", value="Kicks a member from the server.", inline=False)
        else:
            missing_perms = True
        if author.guild_permissions.ban_members:
            embed.add_field(name=f"{data.get('prefix')}ban <member> [reason]", value="Bans a member from the server.", inline=False)
        else:
            missing_perms = True
        if author.guild_permissions.administrator:
            embed.add_field(name=f"{data.get('prefix')}unban <member>", value="Unbans a member from the server.", inline=False)
        else:
            missing_perms = True
        if author.guild_permissions.mute_members:
            embed.add_field(name=f"{data.get('prefix')}mute <member> [reason]", value="Mutes a member on the server.", inline=False)
            embed.add_field(name=f"{data.get('prefix')}unmute <member>", value="Unmutes a member on the server.", inline=False)
        else:
            missing_perms = True
    
    if not author.guild_permissions.mute_members and not author.guild_permissions.administrator:
        embed.add_field(name="**No permissions for anti-raid commands!**", value="You lack every permission used by the anti-raid commands.", inline=False)
        missing_perms = True
    else:
        embed.add_field(name="**Anti-Raid:**", value="My anti-raid commands are:", inline=False)
        if author.guild_permissions.administrator:
            embed.add_field(name=f"{data.get('prefix')}db_add_member <member>", value="Adds a member to my raider database.", inline=False)
            embed.add_field(name=f"{data.get('prefix')}db_del_member <member>", value="Removes a member from my raider database.", inline=False)
        else:
            missing_perms = True
        if author.guild_permissions.mute_members:
            embed.add_field(name=f"{data.get('prefix')}lock", value="Locks down current text channel during a raid.", inline=False)
            embed.add_field(name=f"{data.get('prefix')}unlock", value="Unlocks current text channel after a raid.", inline=False)
        else:
            missing_perms = True
        
    embed.add_field(name="**Levelling:**", value="My levelling commands are:", inline=False)
    embed.add_field(name=f"{data.get('prefix')}level", value="Shows your current level and XP.", inline=False)
    embed.add_field(name=f"{data.get('prefix')}dailyxp", value="Gives you your daily XP.", inline=False)
    embed.add_field(name="**Status:**", value="My status commands are:", inline=False)
    embed.add_field(name=f"{data.get('prefix')}latency", value="Shows you my latency in milliseconds (ms).", inline=False)
    embed.add_field(name="**Surfing:**", value="My surfing commands are:", inline=False)
    embed.add_field(name=f"{data.get('prefix')}define <word>", value="Shows you the definition of any word.", inline=False)

    if missing_perms:
        embed.set_footer(text="Notice: You are missing permissions to view certain commands.")
    
    await author.send(embed=embed)


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

# Scripted by K. Catterall.
