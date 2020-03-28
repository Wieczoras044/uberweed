import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.command()
async def uberweed(ctx, arg):
    channel = ctx.author.voice.channel
    order = arg.split(",")
    if(order[1].isdigit()):
        await ctx.send('Zamówienie przyjęto na '+ order[0].capitalize() + ', ' + str(round(float(order[1])/30,2)) + ' gieta.', tts=True)
        if(ctx.voice_client is None):
            await channel.connect()
        else:
            await ctx.send('Przepraszamy obecnie kurier dostarcza przesyłkę, jesteś w kolejce.')
            await asyncio.sleep(5)
            await ctx.voice_client.disconnect()
            await asyncio.sleep(5)
            await channel.connect()
            await asyncio.sleep(2)
            await ctx.send('Zamówienie zostało dostarczone :)!')
    else:
        await ctx.send('Błąd, poprawne podanie zamówienie to "!uberweed (miejsce),(kwota)"!')

@bot.command()
async def ile(ctx, arg):
    if(arg.isdigit()):
        await ctx.send('Za ' + arg + 'PLN kupisz ' + str(round(float(arg)/30,2)) + ' gieta.')
    else:
        await ctx.send('Podałeś nieprawidłową cene.')


bot.run(os.environ['DISCORD_TOKEN'])

