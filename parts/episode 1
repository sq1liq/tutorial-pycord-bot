import discord
from discord.ext import commands
import dotenv
import os



bot = commands.Bot(intents=discord.Intents.all(),command_prefix='n!')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

@bot.command()
async def hello(ctx:commands.Context):
    await ctx.reply(f"hello {ctx.author.mention} now you are my friend")



bot.run("Your Bot token")
#You get the discord bot token from this website: https://discord.com/developers/applications
