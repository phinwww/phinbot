import requests
import os
import shutil
from qobuz_dl.core import QobuzDL
from discord.ext import commands
import json
import random
from dotenv import load_dotenv

load_dotenv()

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}


class Qobuz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def qobuz(self, ctx, arg1, *args):

        async with ctx.typing():

            email = os.getenv('QOBUZ_USER')
            password = os.getenv('QOBUZ_PASS')
            qobuz = QobuzDL()
            qobuz.get_tokens()
            qobuz.initialize_client(email, password, qobuz.app_id, qobuz.secrets)

            if arg1 == 'd':

                dlurl = ', '.join(args)
                qobuz.handle_url(dlurl)

                directory = 'Qobuz Downloads'
                zipdir = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)
                filename = str(random.randint(0,9999999999999))
                filetype = '.zip'
                print(zipdir)

                shutil.make_archive(filename, 'zip', zipdir)
                with open(filename + filetype, 'rb') as f:
                    data = f.read()
                apiurl = "https://pixeldrain.com/api/file/"
                response = requests.put(apiurl + filename + filetype, data=data)
                json = response.json()
                fileid = json["id"]
                pixeldrain = "https://pixeldrain.com/u/"

                await ctx.reply(pixeldrain + fileid)
                os.remove(filename + filetype)

            elif arg1 == 'l':

                dlquery = ' '.join(args)
                qobuz.lucky_mode(dlquery)

                directory = 'Qobuz Downloads'
                zipdir = max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)
                filename = str(random.randint(0,9999999999999))
                filetype = '.zip'
                print(zipdir)

                shutil.make_archive(filename, 'zip', zipdir)
                with open(filename + filetype, 'rb') as f:
                    data = f.read()
                apiurl = "https://pixeldrain.com/api/file/"
                response = requests.put(apiurl + filename + filetype, data=data)
                json = response.json()
                fileid = json["id"]
                pixeldrain = "https://pixeldrain.com/u/"

                await ctx.reply(pixeldrain + fileid)
                os.remove(filename + filetype)
            else:
                await ctx.reply("invalid argument, did you forget to type .qobuz d for standard mode or .qobuz l for lucky mode?")


async def setup(client):
    await client.add_cog(Qobuz(client))
