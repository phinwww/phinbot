import requests
import re
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

class Soyjak(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def soyjak(self, ctx):
        async with ctx.typing():

            page = requests.get('https://booru.soy/post/list')
            soup = BeautifulSoup(page.content, 'html.parser')
            child_soup = str(soup.find('section', id="Random_Gemleft"))
            s1 = slice(180, 197)
            result = (child_soup[s1])
            result = result.replace('"', '')
            result = result.replace('<', '')
            result = result.replace('>', '')
            baseurl = "https://booru.soy/"
            page = requests.get(baseurl + result)
            soup = BeautifulSoup(page.content, 'html.parser')
            child_soup = str(soup.find('img', id="main_image"))
            s1 = slice(2, 67)
            src = child_soup.split('src=',1)[1]
            src = (src[s1])
            src = src.replace('"', '')
        await ctx.reply(baseurl + src)

async def setup(client):
    await client.add_cog(Soyjak(client))
