import helper
from time import sleep

bot = helper.bot


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


def voice_connection(context):
    if context.author.voice is None:
        raise TypeError


@bot.command()
async def bonk(context):
    try:
        voice_connection(context)
    except TypeError:
        await context.send(context.author.name + " no está en ningun canal de voz... Bonk para ti", tts=True)
        return

    voice_channel = context.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(helper.bonk_file())
    # Sleep while audio is playing.
    while vc.is_playing():
        sleep(.1)
    await vc.disconnect()
    # Delete command after the audio is done playing.
    await context.message.delete()


@bot.command()
async def metase(ctx, *, member: helper.discord.Member):
    await ctx.send("Metase {0}... pero el finger, ja ja ja".format(member.mention), tts=True)


@bot.command()
async def perseguidos(context):
    try:
        voice_connection(context)
    except TypeError:
        await context.send(context.author.name + " no está siendo perseguido")
        return

    voice_channel = context.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(helper.chasing())
    # Sleep while audio is playing.
    while vc.is_playing():
        sleep(.1)
    await vc.disconnect()
    # Delete command after the audls io is done playing.
    await context.message.delete()

bot.run(helper.token)
