import discord
from discord.message import Message

from rules import valid_prizepick, valid_channel_and_guild
from ui import pp_message, pp_history

from enum import Enum
from dataclasses import dataclass
import os

from selenium import webdriver


@dataclass
class ProSlip:
    confidence: float | None
    link: str | None
    author: str | None


pending_picks = dict()

client = discord.Client()

# ======= [ CLIENT ] =======


@client.event
async def on_ready():
    print("Logged in as", client.user)


@client.event
async def on_message(message: Message):
    if not isinstance(message.channel, discord.TextChannel):
        return

    if not valid_channel_and_guild(message):
        print("Not valid guild and channel:", message.channel.id)
        return

    if not valid_prizepick(message.content):
        print("Not valid prizepick:", message.content)
        return

    slip = ProSlip()
    slip.link

    await message.add_reaction("🌭")
    await pp_history(message.channel, limit=4)


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()

    TOKEN = os.getenv("TOKEN")

    if TOKEN is not None:
        client.run(TOKEN)
