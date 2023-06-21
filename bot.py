import os

import discord
intents = discord.Intents.all()

from dotenv import load_dotenv

from discord.ext import commands
from cogwatch import Watcher


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GAME = os.getenv('DISCORD_GAME')

client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(GAME))
    print(f'{client.user} is up running phinbot')

    watcher = Watcher(client, path='cogs', preload=True, debug=False)
    await watcher.start()

client.run(TOKEN)
