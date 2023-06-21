import requests
from discord.ext import commands

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}


class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, arg1, arg2, *args):

        data = {
            'q': ' '.join(args),
            'source': arg1,
            'target': arg2,
        }

        response = requests.post('https://translate.argosopentech.com/translate', headers=headers, data=data)
        json = response.json()
        await ctx.reply(json["translatedText"])


async def setup(client):
    await client.add_cog(Translate(client))
