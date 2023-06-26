import subprocess
from discord.ext import commands

class Bash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def bash(self, ctx, *args):

        bashcmd = ' '.join(args)
        process = subprocess.run(bashcmd,shell=True,capture_output=True,text=True)
        quotes = "```"
        processout = str(process.stdout)
        await ctx.reply(quotes + processout + quotes)

async def setup(client):
   await client.add_cog(Bash(client))
