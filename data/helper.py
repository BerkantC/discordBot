import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging

load_dotenv()
bot = commands.Bot(command_prefix='$')
logging.basicConfig(level=logging.INFO)


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

token = os.getenv('TOKEN')
