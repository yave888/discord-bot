# auto_response.py

import discord

async def send_separator(channel):
    separator_line = "-" * 100
    await channel.send(separator_line)

async def on_message_auto_response(message: discord.Message):
    if message.author.bot:
        return

    content = message.content.lower()
    if "きりとり線" in content or "きりとり" in content:
        await send_separator(message.channel)