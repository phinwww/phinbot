import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason: str):
        if reason is None:
            await member.kick()
            await ctx.reply(f'{member} was kicked.')
        else:
            await member.kick(reason=reason)
            await ctx.send(f"**{member}** has been kicked for **{reason}**.")


    @kick.error
    async def kick_error(error, ctx):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to do that!")


async def setup(client):
    await client.add_cog(Kick(client))
