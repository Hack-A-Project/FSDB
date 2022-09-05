import os
import logging
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

bot = discord.Bot()

@bot.event
async def on_ready():
  print(f'{bot.user} is ready and online!')

@bot.slash_command(name = "fs", description="something")
async def fsd(ctx, text):
  print(text)
  await ctx.respond("hey!")

bot.run(TOKEN)