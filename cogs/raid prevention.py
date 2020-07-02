# Stealth bot scripted created by K. Catterall.

import discord
from discord.ext import commands

class RaidPrevention(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Add a member from an "anti-raid database" (Fake command = Stealth).
    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def db_add_member(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.send(f'{member} has been added to the raid database.')
        except:
            await ctx.send(f'{member} not found on current guild.')
    

    # Remove a member from an "anti-raid database" (Fake command = Stealth).
    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def db_del_member(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.send(f'{member} has been removed from the raid database.')
        except:
            await ctx.send(f'{member} not found on current guild.')
    

    # Lock a channel (Trustworhy command = Stealth).
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)}
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"Channel `{channel.name}` locked down.")
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"Channel `{channel.name}` locked down.")


    # Unlock a channel (Trustworhy command = Stealth).
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(send_messages=True)}
            await channel.edit(overwrites=overwrites)
            await ctx.send(f"Channel `{channel.name}` unlocked.")
        elif channel.overwrites[ctx.guild.default_role].send_messages == None or channel.overwrites[ctx.guild.default_role].send_messages == False:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(f"Channel `{channel.name}` unlocked.")


def setup(client):
    client.add_cog(RaidPrevention(client))


# Stealth bot scripted created by K. Catterall.
