import discord
import os
from keep_alive import keep_alive
from wordle import processGuess

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: return

  msg=message.content
  if msg.startswith('$hello'):
    await message.channel.send('Hello world!')

  if msg.startswith('$dm'):
    return #not implemented for now
    #channel = await message.author.create_dm()
    #await channel.send('Welcome to Ace Attordle Bot! Enter *$help* for instructions!')

  if msg.startswith('$aa'):
    args = msg.split("$aa",1)[1]
    await message.channel.send(processGuess(args))
    return

keep_alive()

client.run(os.getenv('TOKEN'))