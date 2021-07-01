import discord
from discord.ext import commands, tasks
from random import choice

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print('Alias Bot is online!')


@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['Why did you wake me up?',
                 'Top of the World!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))


@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['Dead dope',
                 'I could have done so much more', 'Lol, bye!']
    await ctx.send(choice(responses))


client.run('TOKEN')
