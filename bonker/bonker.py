from data import helper
from time import sleep

bot = helper.bot


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


async def play_file(context, file):
    try:
        if context.author.voice is None:
            raise TypeError
    except TypeError:
        await context.send(context.author.name + " no está en ningun canal de voz... Bonk para ti", tts=True)
        return

    voice_channel = context.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(file)
    # Sleep while audio is playing.
    while vc.is_playing():
        sleep(.1)
    await vc.disconnect()
    # Delete command after the audio is done playing.
    await context.message.delete()


@bot.command()
async def bonk(context):
    file = helper.bonk_file()
    await play_file(context, file)


@bot.command()
async def perseguidos(context):
    file = helper.chasing()
    await play_file(context, file)


@bot.command()
async def metase(ctx, *, member: helper.discord.Member):
    await ctx.send("Metase {0}... pero el finger, ja ja ja".format(member.mention), tts=True)


bot.run(helper.token)
