import discord
from discord.ui import View, Button
import os

intents = discord.Intents.default()
intents.message_content = True  # MUST be enabled in Dev Portal too

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore bot messages
    if message.author.bot:
        return

    msg = message.content.lower()

    # Trigger if "code" OR "link" is ANYWHERE in message
    if any(word in msg for word in ["code", "link"]):

        embed = discord.Embed(
            title="📌 Server Code",
            description="**Code:** `dqqaph8z`",
            color=discord.Color.green()
        )
        embed.set_footer(text="Powered by SRP | SERIOUS ROLEPLAY")

        view = View()
        button = Button(
            label="Quick Join",
            url="https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Ddqqaph8z",
            style=discord.ButtonStyle.link,
            emoji="🔗"
        )
        view.add_item(button)

        await message.channel.send(embed=embed, view=view)

client.run(os.getenv("TOKEN"))
