from discord.ext import commands
import discord
import config
from random_commands import roll_dice, pon
from help_command import custom_help
from timer_commands import start_timer, end_timer, pause_timer, check_time
from auto_response import on_message_auto_response


intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(
    command_prefix="$",
    case_insensitive=True,
    intents=intents
)

@bot.event
async def on_ready():
    print("Bot is ready!")
    print("Registered commands:")
    for command in bot.commands:
        print(command.name)

@bot.event
async def on_message(message: discord.Message):
    await on_message_auto_response(message)
    await bot.process_commands(message)

# dice コマンド
bot.add_command(roll_dice)

# じゃんけん コマンド
bot.add_command(pon)

# 独自のヘルプコマンド
bot.add_command(custom_help)

# タイマー管理コマンド
bot.add_command(start_timer)
bot.add_command(end_timer)
bot.add_command(pause_timer)
bot.add_command(check_time)

# token
bot.run(config.TOKEN)
