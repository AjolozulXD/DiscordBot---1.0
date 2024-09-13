import discord
import settings
from bot_logic import gen_pass
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Holas")
    elif message.content.startswith('$chau'):
        await message.channel.send("Chau, hermos@!")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass (10))
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")
    
client.run("MTI4MTc4MDU5NDQ1NTQ4MjQ2Mw.Gi1sA2.mZXzIA9BoP84arUsZo5IFpG9lY9Ycf6VC9Hc6A")

client.run(settings["MTI4MTc4MDU5NDQ1NTQ4MjQ2Mw.Gi1sA2.mZXzIA9BoP84arUsZo5IFpG9lY9Ycf6VC9Hc6A"])