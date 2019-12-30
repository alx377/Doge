
from discord.ext import commands
from discord import utils, FFmpegPCMAudio
import discord
import asyncio
import os
import random

BASE_DIR = "mp3"

def find_file_name(query):
    files = []
    for f_name in os.listdir(BASE_DIR):
        if query in f_name:
            files.append(f_name)
    if files:
        return f"{BASE_DIR}/{random.choice(files)}"
    return None

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    guild = utils.get(client.guilds, name="Doges of War")
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild}'
    )

@client.command(
    name='doge',
    description='Searches for audio file and plays it in the voice channel',
    pass_context=True,
)
async def doge(context, arg):
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.channel
    channel = None
    if voice_channel != None:
        file_name = find_file_name(arg)
        if file_name:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            source = discord.FFmpegPCMAudio(file_name)
            vc.play(source)
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.stop()
            await vc.disconnect()
        else:
            await context.send(f'No results for query "{arg}"')
    else:
        await context.send('User is not in a voice channel.')

@client.command(
    name='dogelist',
    description='Searches for audio file and plays it in the voice channel',
    pass_context=True,
)
async def dogelist(ctx):
    filenames = []
    for f_name in os.listdir(BASE_DIR):
        filenames.append(f_name.split(".")[0])
    filenames = sorted(filenames)
    await ctx.send("\n".join(filenames))

client.run(os.getenv("DOGE_TOKEN"))
