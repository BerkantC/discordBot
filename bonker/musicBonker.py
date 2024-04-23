import asyncio

from data import helper
from data import Banned
from datetime import datetime, timedelta
from discord.ext import commands,tasks
import discord
from discord import Color
from pytube import Search
from pytube import YouTube
import os
import shutil


intents = discord
bot = helper.bot


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


def give_link(name): # Youtube has different ids for each video. So we are finding those to download vids.
    s = Search(f"{name}")  #searching from title of the yt vid
    yt_id = s.results #this gives us a list
    video_ids = [video.video_id for video in yt_id] #scraping the data that we want

    video_id = video_ids[0] #getting the first element
    base_url = f"https://www.youtube.com/watch?v={video_id}" #making our link ready
    return base_url


def download_vid(name):
    s = Search(f"{name}")
    yt_id = s.results
    video_ids = [video.video_id for video in yt_id]

    video_id = video_ids[0]
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(base_url)
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first() #downloading the first Result and only mp4
    audio_stream.download(output_path='music') # we are deciding where we want to install


def delete_audio():
    shutil.rmtree('music')


def find_music_name():
    return os.listdir("music")[0]


def remove_all_files(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():  # if the music is already playing
        ctx.voice_client.pause()  # pausing the music
        await ctx.send("Playback paused.")  # sending confirmation on  channel
    else:
        await ctx.send(
            '[-] An error occured: You have to be in voice channel to use this commmand')  # if you are not in vc


@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():  # If the music is already paused
        ctx.voice_client.resume()  # resuming the music
        await ctx.send("Playback resumed.")  # sending confirmation on  channel
    else:
        await ctx.send(
            '[-] An error occured: You have to be in voice channel to use this commmand')  # if you are not in vc


@bot.command()
async def leave(ctx):
    if ctx.voice_client:  # if you are in vc
        await ctx.guild.voice_client.disconnect()  # disconnecting from the vc
        await ctx.send("Lefted the voice channel")  # sending confirmation on channel
        sleep(1)
        remove_all_files(
            "music")  # deleting the all the files in the folder that  we downloaded to not waste space on your pc

    else:
        await ctx.send(
            "[-] An Error occured: You have to be in a voice channel to run this command")  # if you are not in vc


@bot.command()
async def join(context):
    if context.author.voice:
        channel = context.message.author.voice.channel
        try:

            await channel.connect()  # connecting to channel
        except:
            await context.send("[-] An error occured: Couldn't connect to the channel")  # if there is an error

    else:
        await context.send("[-] An Error occured: You have to be in a voice channel to run this command") #if you are not in vc


@bot.command(name="play")
async def play(ctx, *, title):
    download_vid(title)  # Downloading the mp4 of the desired vid
    voice_channel = ctx.author.voice.channel

    if not ctx.voice_client:  # if you are not in  vc
        voice_channel = await voice_channel.connect()  # connecting to vc

    try:
        async with ctx.typing():
            player = discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\ffmpeg.exe",
                                            source=f"music/{find_music_name()}")  # executable part is where we downloaded ffmpeg. We are writing our find_mmusic name func because , we want to bot to play our desired song fro the folder
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send(f'Now playing: {find_music_name()}')  # sening confirmmation

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
        delete_selected_file(find_music_name())  # deleting the file after it played

    except Exception as e:
        await ctx.send(f'Error: {e}')  # sending error
bot.run(helper.token)