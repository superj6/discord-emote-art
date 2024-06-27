from ascii_templater import ascii_templates

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
async def emojitext(ctx, emoji: str, phrase: str, spacelen: int = 6):
    ret = ''

    filtered_phrase = ''.join(letter.lower() if letter.lower() in ascii_templates else '-' for letter in phrase)

    for i in range(5):
        for letter in filtered_phrase:
            ret += \
                    ascii_templates[letter]\
                    .splitlines()[i]\
                    .format(spacer = ' ' * spacelen, template_char = emoji)
            ret += ' ' * 3

        ret += '\n'

    if ret[0] == ' ':
        ret = '.' + ret[1:]

    await ctx.send(ret)

bot.run(os.environ['DISCORD_TOKEN'])

