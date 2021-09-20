from data import helper
from time import sleep

bot = helper.bot


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


def get_bot_vc(ctx):
    return helper.discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)


async def play_file(context, file):
    try:
        if context.author.voice is None:
            raise TypeError
    except TypeError:
        await context.send(context.author.name + " no está en ningun canal de voz... Bonk para ti", tts=True)
        return

    bot_vc = get_bot_vc(context)

    if bot_vc is None:
        vc = await context.author.voice.channel.connect()
    else:
        vc = bot_vc
    vc.play(file)
    # Sleep while audio is playing.
    while vc.is_playing():
        sleep(.1)
    await vc.disconnect()
    # Delete command after the audio is done playing.
    await context.message.delete()


@bot.command(brief="Dale un Bonk al chat de voz")
async def bonk(context):
    file = helper.bonk_file()
    await play_file(context, file)


@bot.command(brief="Te persiguen en DbD?")
async def perseguidos(context):
    file = helper.chasing()
    await play_file(context, file)


@bot.command(brief="Etiqueta a tus amigos para jugar")
async def metase(ctx, *, member: helper.discord.Member):
    await ctx.send("Metase {0}... pero el finger, ja ja ja".format(member.mention), tts=True)

bot.run(helper.token)
