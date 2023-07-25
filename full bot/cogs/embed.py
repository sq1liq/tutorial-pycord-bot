import discord
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx: commands.Context, *, descr: str):
        embed = discord.Embed(
            title="Embed",
            description=descr,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1093624171235377194/1093833717014867998/Bild_2023-04-06_230517912.png")
        embed.set_author(name=f"from {ctx.guild.name}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(embed(bot))
