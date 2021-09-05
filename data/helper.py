import logging
import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = commands.Bot(command_prefix='$')
ffmpegLib = os.fspath("ffmpeg\\bin\\ffmpeg")


def bonk_file():
    return discord.FFmpegPCMAudio(source=Path('bonker\\bonk.mp3'), executable=ffmpegLib)


def chasing():
    return discord.FFmpegPCMAudio(source=Path('bonker\\bonk.mp3'), executable=ffmpegLib)


token = os.getenv('TOKEN')
print("helper imported")
