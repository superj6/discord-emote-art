import ascii_templater as temper

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
    spacer = ' ' * spacelen

    filt_phrase = ''.join(letter.lower() if temper.has_template(letter.lower()) else '-' for letter in phrase)

    t = 0
    messages = []
    while t < len(filt_phrase):
        tt = t
        while tt < len(filt_phrase) \
                and tt - t < 15 \
                and len(temper.fill_template_phrase(filt_phrase[t:tt + 1], spacer, emoji)) < 2000:
            tt += 1
        
        messages.append(temper.fill_template_phrase(filt_phrase[t:tt], spacer, emoji))

        t = tt

        if len(messages) > 3:
            await ctx.send('too long message!')
            return

    for message in messages:
        await ctx.send(message)

bot.run(os.environ['DISCORD_TOKEN'])

