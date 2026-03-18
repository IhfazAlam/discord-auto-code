import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if "code" in msg or "link" in msg:
        embed = discord.Embed(
            title="Server Code",
            description="Code: `d5aucw7g`\n\nPowered by SRP | SERIOUS ROLEPLAY",
            color=discord.Color.green()
        )
        await message.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
