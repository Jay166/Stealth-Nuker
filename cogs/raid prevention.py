import discord
from discord.ext import commands

class RaidPrevention(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def db_add_user(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.send(f'{member} has been added to the raid database.')
        except:
            await ctx.send(f'{member} not found on current guild.')
    

    @commands.command()
    async def db_del_user(self, ctx, member : discord.Member, *, reason=None):
        try:
            await ctx.send(f'{member} has been removed from the raid database.')
        except:
            await ctx.send(f'{member} not found on current guild.')


def setup(client):
    client.add_cog(RaidPrevention(client))
