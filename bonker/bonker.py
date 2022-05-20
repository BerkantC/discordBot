from data import helper
from data import Banned
from datetime import datetime, timedelta

bot = helper.bot
bannedMembers = {}


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


async def should_allow_message_from_author(context):
    if context.author.id in bannedMembers:
        seconds = (bannedMembers[context.author.id].time-datetime.now()).seconds
        await context.send("{0}, nel pa, te quedan {1} segundos de silencio".format(context.author.mention, seconds))
        return False
    else:
        return True


async def get_vc(context):
    bot_vc = helper.discord.utils.get(context.bot.voice_clients, guild=context.guild)
    if bot_vc is None:
        return await context.author.voice.channel.connect()
    else:
        return bot_vc


async def check_user_prerequisites(context):
    if not await should_allow_message_from_author(context):
        return False

    try:
        if context.author.voice is None:
            raise TypeError
    except TypeError:
        await context.send(context.author.name + " no está en ningun canal de voz... Bonk para ti", tts=True)
        return False

    return True


async def play_file(context, file):
    if not await check_user_prerequisites(context):
        return

    vc = await get_vc(context)

    if vc.is_playing():
        return

    vc.play(file)
    # Sleep while audio is playing.
    while vc.is_playing():
        helper.sleep(1)
    await vc.disconnect()
    # Delete command after the audio is done playing.
    await context.message.delete()


@bot.command(brief="Dale un Bonk al chat de voz")
async def bonk(context):
    file = helper.bonk_file()
    await play_file(context, file)


@bot.command(brief="Te persiguen en DbD?")
async def perseguidos(context):
    if not await check_user_prerequisites(context):
        return

    file = helper.chasing()
    vc = await get_vc(context)

    await helper.run_blocking(helper.play_non_blocking, context, file, vc)
    await vc.disconnect()
    await context.message.delete()


@bot.command(brief="Alguien anda de ruidoso?")
async def callate(context):
    file = helper.shutup()
    await play_file(context, file)


@bot.command(brief="SIUUUUUUUUU")
async def siu(context):
    file = helper.siu()
    await play_file(context, file)


@bot.command()
async def bitconnect(context):
    file = helper.bitconnect()
    await play_file(context, file)


@bot.command(brief="AAAAAAAAA")
async def a(context):
    file = helper.a()
    await play_file(context, file)


@bot.command()
async def w(context):
    file = helper.fanfare()
    await play_file(context, file)


@bot.command()
async def victory(context):
    file = helper.victory()
    await play_file(context, file)


@bot.command(brief="Etiqueta a tus amigos para jugar")
async def metase(ctx, *, member: helper.discord.Member):
    await ctx.send("Metase {0}... pero el finger, ja ja ja".format(member.mention), tts=True)


@bot.command(brief="nuker!")
async def clear(ctx, number):
    if helper.ISDEV is True:
        number = int(number)
        await ctx.channel.purge(limit=number)


@bot.command(brief="Silencia a alguien por X segundos")
async def timeout(ctx, member: helper.discord.Member, timeInterval: int):
    if timeInterval > 60:
        await ctx.send("No te pases de verga XD tampoco es ban para toda la vida...")
        return

    unBanDateTime = datetime.now() + timedelta(seconds=timeInterval)
    bannedMember = Banned.Banned(ctx.channel, member, unBanDateTime)
    bannedMembers[member.id] = bannedMember
    message = "{0}, te vas a la banca por {1} segundos".format(member.mention, timeInterval)
    await ctx.send(message)


@bot.command(brief="quitar el silencio de alguien")
async def unban(ctx, *, member: helper.discord.Member):
    bannedMembers.pop(member.id)
    await ctx.send("si {0} estaba baneado... pues ya no".format(member.mention))


@helper.tasks.loop(seconds=5)
async def unban():
    for key in list(bannedMembers):
        if bannedMembers[key].time <= datetime.now():
            member = bannedMembers[key]
            channel = member.channel
            await(channel.send("{0} ya puede enviar mensajes".format(member.name.mention)))
            del bannedMembers[key]


unban.start()
bot.run(helper.token)
