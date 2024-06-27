import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def emojitext(ctx, emoji: str,  phrase: str):
    await ctx.send(f'{emoji} {emoji}')

bot.run(os.environ['DISCORD_TOKEN'])

