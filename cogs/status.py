# Stealth bot scripted created by K. Catterall.

import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    # Display latency (Trustworthy command = Stealth).
    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f'Atom latency: {round(self.client.latency*1000)}ms.')


def setup(client):
    client.add_cog(Status(client))


# Stealth bot scripted created by K. Catterall.
