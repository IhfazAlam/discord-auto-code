import discord
from discord.ui import View, Button
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()
    if "code" in msg or "link" in msg:

        # Embed
        embed = discord.Embed(
            title="📌 Server Code",
            description="**Code:** `d5aucw7g`",
            color=discord.Color.green()  # GREEN COLOR
        )
        embed.set_footer(text="Powered by SRP | SERIOUS ROLEPLAY")

        # Button with emoji
        view = View()
        button = Button(
            label="Quick Join",
            url="https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Dyd5bq4tu",  # Replace with your link
            style=discord.ButtonStyle.link,
            emoji="🔗"
        )
        view.add_item(button)

        await message.channel.send(embed=embed, view=view)

client.run(os.getenv("TOKEN"))
