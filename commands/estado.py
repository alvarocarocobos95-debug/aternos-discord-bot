import discord
from discord.ext import commands
from discord import app_commands


class Estado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="estado",
        description="Muestra el estado del servidor."
    )
    async def estado(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🟢 Estado del servidor",
            description="El sistema de comandos funciona correctamente.",
            color=discord.Color.green()
        )

        embed.set_footer(text="Minecraft 26 Assistant")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Estado(bot))