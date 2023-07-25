import discord
from discord.ext import commands
import dotenv
import os



bot = commands.Bot(intents=discord.Intents.all(),command_prefix='n!')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}") # print the bot's name in the console


#first command
@bot.command()
async def hello(ctx:commands.Context):
    await ctx.reply(f"hello {ctx.author.mention} now you are my friend")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename[:-3]}")






dotenv.load_dotenv()
bot.run(os.getenv("TOKEN"))
