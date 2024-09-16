import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"機器人已登入為 {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(TOKEN)
