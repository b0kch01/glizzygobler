from discord import TextChannel
from dataclasses import dataclass


ACCEPTABLE_CHANNELS = [1341888392627097716]
ACCEPTABLE_GUILDS = [1341888392627097713]
ACCEPTABLE_ROLES = ["@&1341949739259658242"]


@dataclass
class ProSlip:
    confidence: float | None
    link: str | None
    author: str | None


def valid_prizepick(string):
    return any((
        *[tag in string for tag in ACCEPTABLE_ROLES],
        "https://prizepicks.onelink.me/gCQS/shareEntry?entryId=" in string,
    ))


def valid_channel_and_guild(message):
    return all((
        message.channel.id in ACCEPTABLE_CHANNELS,
        message.guild.id in ACCEPTABLE_GUILDS))
