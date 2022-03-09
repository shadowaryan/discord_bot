import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

client = commands.Bot(command_prefix = '$')


#login event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#join event
@client.event
async def on_member_join(member):
    print(f'{member} joined the server')

#remove event
@client.event
async def on_member_remove(member):
    print(f'{member} left the server')

@client.command()
async def stats(message):
    # if message.author == client.user:
    #     return

    id = client.get_guild(950674739133808690)

    # if message.content.startswith('$hello'):
    #     slug = message.content.partition('')[2]
    #     print(slug)
    #     await message.channel.send('Hello!')

    # if message.content.startswith('$server_stats'):
    await message.send(f' Server Stats:-\n no of member: {id.member_count}')
  
@client.command()
async def nft(message,*,slug):
    response = requests.get(f'https://api.opensea.io/collection/{slug}/stats').json()['stats']
    await message.send(f'Slug Name:-{slug}\nThere Stats:-\n\n{response}')
    

load_dotenv()
client.run(os.getenv('TOKEN'))
