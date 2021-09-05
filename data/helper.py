import logging
import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='$')


def bonk_file():
    return discord.FFmpegPCMAudio(source=Path('bonker/bonk.mp3'))


def chasing():
    return discord.FFmpegPCMAudio(source=Path('bonker/chasing.mp3'))


token = os.getenv('TOKEN')
