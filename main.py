import discord
import random
from discord.ext import commands

from datetime import date
f_date = date(2021, 6, 26)
l_date = date.today()
delta = l_date - f_date
print(delta.days)

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print('Bot is ready.')

@client.command()
async def ping(ctx):
	await ctx.send(f'It has been {delta.days} days since this bot was created!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user: #Bot only replies to real users
        return


    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
	
	
    shower_thoughts = ['It kinda makes sense that the target audience for fidget spinners lost interest in them so quickly.','Peer pressure as an adult is seeing your neighbor mow their lawn.','If humans could fly, we would consider it exercise and never do it.','Pavlov probably thought about feeding his dogs every time someone rang a bell','Thermometers are speedometers for atoms.','Baby Yoda\'s first word probably came after his second word.']

    if message.content == '!shower':
        response = random.choice(shower_thoughts)
        await message.channel.send(response)

client.run('-client-code-goes-here')
