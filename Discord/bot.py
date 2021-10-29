import json
import requests

import discord
from discord.ext import commands
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def join(ctx):
    data = {
        'max_age': 86400,
        'max_uses': 0,
        'target_application_id': 755600276941176913,
        'target_type': 2,
        'temporary': False,
        'validate': None,
    }
    headers = {
        'Authorization': 'Bot ODc3OTk2MzMxMDk0OTIxMjg2.YR6vzQ.uNNEs005kFRO1SASgRvgRHO-2Kc',
        'Content-Type': 'application/json'
    }

    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else: await ctx.send('**Enter the channel**')
    else: await ctx.send('**Enter the channel**')

    responce = requests.post(f'https://discord.com/api/v8/channels/{channel}/invites', data=json.dumps(data), headers=headers)
    link = json.loads(responce.content)

    await ctx.send(f'https://discord.com/invite/{link["code"]}')

bot.run('ODc3OTk2MzMxMDk0OTIxMjg2.YR6vzQ.uNNEs005kFRO1SASgRvgRHO-2Kc')