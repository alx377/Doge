
from discord.ext import commands
from discord import utils, FFmpegPCMAudio
import discord
import asyncio
import os
import random

BASE_DIR = "mp3"
GUILD = os.getenv("GUILD", "Doges of War")

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
    guild = utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild}'
    )

@client.command(
    name='doge',
    description='Searches for audio file and plays it in the voice channel',
    pass_ctx=True,
)
async def doge(ctx, arg):
    # Get file first
    file_name = find_file_name(arg)
    if not file_name:
        await ctx.send(f'No results for query "{arg}". Try command !dogelist.')
        return
    # If already on channel use that one
    vc = utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    # If not connect to users channel
    if not vc:
        user = ctx.message.author
        voice_channel = user.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
        else:
            await ctx.send('User is not in a voice channel.')
            return

    source = discord.FFmpegPCMAudio(file_name)
    vc.play(source)
    while vc.is_playing():
        await asyncio.sleep(1)
    vc.stop()

@client.command(
    name='dogelist',
    description='Searches for audio file and plays it in the voice channel',
    pass_ctx=True,
)
async def dogelist(ctx):
    filenames = []
    for f_name in os.listdir(BASE_DIR):
        filenames.append(f_name.split(".")[0])
    filenames = sorted(filenames)
    await ctx.send("\n".join(filenames))

@client.command(
    name='dogejoin',
    description='Force Doge to join to voice channel for one hour',
    pass_ctx=True,
)
async def dogejoin(ctx):
    vc = utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    voice_channel = ctx.message.author.voice.channel

    if vc and vc.channel == voice_channel:
        await ctx.send('Already on your channel')
        return

    if vc and vc.channel != voice_channel:
        await vc.move_to(voice_channel)

    if voice_channel != None:
        await voice_channel.connect(timeout=3600)
    else:
        await ctx.send('User is not in a voice channel.')

@client.command(
    name='dogeleave',
    description='Force Doge to join to voice channel for one hour',
    pass_ctx=True,
)
async def dogeleave(ctx):
    vc = ctx.message.guild.voice_client
    await vc.disconnect()

client.run(os.getenv("DOGE_TOKEN"))
