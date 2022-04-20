import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('OTY2MTQyNjQ5OTM5NjU2Nzc1.Yl9cdQ.TvEQEVO858VV0OcTyhTQ_A-10Ag'))