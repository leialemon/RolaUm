#Setup básico
import discord
import os
import random
from discord import message
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
#Token salvo na função Secrets:
my_secret = os.environ['token']

@bot.command()
async def rolar(roll)
  dado = roll.split("d")
  

bot.run(my_secret)