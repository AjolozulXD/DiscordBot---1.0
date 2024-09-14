import discord
import settings
from bot_logic import gen_pass, flip_coin
from discord.ext import commands
import random


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix="B", intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send("holis")
    
@bot.command()
async def chau(ctx):
    await ctx.send("Adiós, hermos@")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def ILoveAxolotls(ctx)
    await ctx.semd("Awww 😍🥰")

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
bot.run("TOKEN")

bot.run(settings["TOKEN"])
