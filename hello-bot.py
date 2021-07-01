import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Alias Bot is online!')

@client.event
async def on_message(message):
    message.content.lower()
    if message.content.startswith("hello"):
        await message.channel.send("Hey, I'm Alias Bot!")

client.run('ODYwMDIwNjg3MTIwMjM2NTg0.YN1Krg.uwC0CamBrOYqvzQJrUVtQjj0x_E')
