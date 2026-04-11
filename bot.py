import discord
from discord.ui import View, Button
import os

intents = discord.Intents.default()
intents.message_content = True  # IMPORTANT

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()
    print(f"Message detected: {msg}")  # DEBUG

    if "code" in msg or "link" in msg:
        print("🔥 Triggered!")  # DEBUG

        embed = discord.Embed(
            title="📌 Server Code",
            description="**Code:** `x5xmd3ww`",
            color=discord.Color.green()
        )
        embed.set_footer(text="Powered by SRP | SERIOUS ROLEPLAY")

        view = View()
        button = Button(
            label="Quick Join",
            url="https://www.roblox.com/games/start?placeId=7711635737&launchData=joinCode%3Dx5xmd3ww",
            style=discord.ButtonStyle.link,
            emoji="🔗"
        )
        view.add_item(button)

        await message.reply(embed=embed, view=view)

client.run(os.getenv("TOKEN"))
