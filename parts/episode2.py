import discord
from discord.ext import commands
import dotenv
import os



bot = commands.Bot(intents=discord.Intents.all(),command_prefix='n!')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


#the command contains a list of the most important arguments for creating embeds.

@bot.command()
async def testembed(ctx: commands.Context):
    embed = discord.Embed(
        title="This is a title",
        description="This is a description",
        color=discord.Color.blue()
    )
    embed.set_author(name=f"from {ctx.guild.name}")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_image(url=ctx.guild.icon.url)
    embed.add_field(name="This is a field 1", value="This is a field value 1")
    embed.add_field(name="This is a field 2", value="This is a field value 2")
    embed.add_field(name="This is a field 3", value="This is a field value 3", inline=False)
    embed.add_field(name="This is a field 4", value="This is a field value 4", inline=False)

    await ctx.send(embed=embed)

#and this comand is to test a embed where you can change the description while you execute this command (Like: n!embed This is a description)


@bot.command()
async def embed(self, ctx: commands.Context, *, descr: str):
    embed = discord.Embed(
        title="Embed",
        description=descr,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1093624171235377194/1093833717014867998/Bild_2023-04-06_230517912.png")
    embed.set_author(name=f"from {ctx.guild.name}")

    await ctx.send(embed=embed)


bot.run("Your Bot token")
#You get the discord bot token from this website: https://discord.com/developers/applications
