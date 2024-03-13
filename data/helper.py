import os
from pathlib import Path

import discord
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from dotenv import load_dotenv
import logging
from time import sleep

import functools
import typing

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
# ISDEV = os.getenv('TOKENDEV') is not None
# if ISDEV:
#     bot = commands.Bot(command_prefix="!")
# else:
bot = commands.Bot(command_prefix='$', intents=intents)
logging.basicConfig(level=logging.DEBUG)


def bonk_file():
    return discord.FFmpegPCMAudio(source=Path('bonker/bonk.mp3'))


def chasing():
    return discord.FFmpegPCMAudio(source=Path('bonker/chasing.mp3'))


def shutup():
    return discord.FFmpegPCMAudio(source=Path('bonker/shutup.mp3'))


def a():
    return discord.FFmpegPCMAudio(source=Path('bonker/scream.mp3'))


def siu():
    return discord.FFmpegPCMAudio(source=Path('bonker/siu.mp3'))


def bitconnect():
    return discord.FFmpegPCMAudio(source=Path('bonker/bitconnect.mp3'))


def fanfare():
    return discord.FFmpegPCMAudio(source=Path('bonker/win.mp3'))


def victory():
    return discord.FFmpegPCMAudio(source=Path('bonker/victory.mp3'))


def trampa():
    return discord.FFmpegPCMAudio(source=Path('bonker/cartatrampa.mp3'))


def play_non_blocking(context, file, vc):
    vc.play(file)
    while vc.is_playing():
        sleep(1)


async def run_blocking(blocking_func: typing.Callable, *args, **kwargs) -> typing.Any:
    func = functools.partial(blocking_func, *args, **kwargs)
    return await bot.loop.run_in_executor(None, func)

# token = os.getenv('TOKENDEV', 'TOKEN')
token = os.getenv('TOKEN')
