import settings
import discord
from discord.ext import commands
from bot_logic import get_duck_image_url
from bot_logic import gen_pass, flip_coin
import random
import yt_dlp
import os

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix="B", intents=intents)

ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

# Comando para saludar
@bot.command()
async def hola(ctx):
    await ctx.send("holis")

# Comando para despedirse
@bot.command()
async def chau(ctx):
    await ctx.send("Adiós, hermos@")

# Comando para generar una contraseña aleatoria
def gen_pass(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

# Comando para tirar una moneda
def flip_coin():
    return random.choice(["Cara", "Cruz"])

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

# Comando especial
@bot.command()
async def ILoveAxolotls(ctx):
    await ctx.send("Awww 😍🥰")

# Comando para tirar dados
@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('El formato tiene que ser NdN (ejemplo: 2d6)!')
        return
    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def mem(ctx):
    with open('images/meme 1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memRandom(ctx):
    memRandom = random.choice(os.listdir("images"))
    with open(f'images/{memRandom}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('patito')
async def patito(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def tec(ctx):
    # Lista de imagenes y probabilidades:
    imagenes_y_pesos = {
        "Limitless.jpg": 60,
        "Construccionç.jpg": 50,
        "Manipulación_de_Cuervos.jpg": 40,
        "Técnica_de_Manipulación_de_Artefactos.jpg": 50,
        "Vudu.jpg": 45,
        "ManipulacionDeMarionetas.jpg": 40,
        "Boogie_Woogie.jpg": 40,

        "Proporcion.jpg": 20,
        "CorrosiónExtrema.jpg": 30,
        "Técnica_de_Necromancia.jpg": 35,
        "Técnica_de_Inmortalidad.jpg": 25,
        "Bestias_Protectoras.jpg": 15.5,
        
        "MutacionLibre.jpg": 5,
        "Volcan.jpg": 10,
        "Ten-Shadows.jpg": 4.5,
        "Técnica_de_Proyección.jpg": 4,
        "Técnica_de_Inverso.jpg": 5,
        "Técnica_de_Formación_de_Hielo.jpg": 3,
        "Técnica_de_El_Cómico.jpg": 1,
        "Discurso_Maldito.jpg": 15.3,
        "Plant.jpg": 5,
        "Curse_Mani.jpg": 3,
        "BloodManipulation.jpg": 5,

        "Dagon.jpg": 2.5,
        "BlackFlash.jpg": 0.01,
        "Mahoraga.jpg": 1.5,
        "SixEyes.jpg": 0.1,
        "Shrine.jpg": 0.1,
        "Idle_Death_Gamble.jpg": 1,

    }

    imagenes = list(imagenes_y_pesos.keys())
    pesos = list(imagenes_y_pesos.values())

    # Selección de imagen con probabilidades
    tec_seleccionada = random.choices(imagenes, pesos, k=1)[0]

    # Ruta completa a la imagen seleccionada
    ruta_imagen = os.path.join("techniques", tec_seleccionada)

    # Abrir y enviar la imagen seleccionada
    with open(ruta_imagen, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("Token")

bot.run(settings["Token"])
