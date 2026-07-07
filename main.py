import discord
from discord.ext import commands
from config import DISCORD_TOKEN
import os
import asyncio
# Configuración de los permisos (intents)
intents = discord.Intents.default()

# Creamos el bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents

)
async def cargar_cogs():
    for archivo in os.listdir("./commands"):
        if archivo.endswith(".py") and archivo != "__init__.py":
            await bot.load_extension(f"commands.{archivo[:-3]}")
            print(f"✅ Cargado: {archivo}")

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    await bot.tree.sync()

    print("=" * 50)
    print(f"🤖 Bot conectado como: {bot.user}")
    print("✅ Minecraft 26 Assistant está listo.")
    print("✅ Slash Commands sincronizados.")
    print("=" * 50)

# Arrancar el bot
async def main():
    async with bot:
        await cargar_cogs()
        await bot.start(DISCORD_TOKEN)

asyncio.run(main())
