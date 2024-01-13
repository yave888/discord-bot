from discord.ext import commands
import random

@commands.command(
    name="dice",
    aliases=["roll"]
)
async def roll_dice(ctx: commands.Context):
    answer = ["1", "2", "3", "4", "5", "6"]
    choice = random.choice(answer)
    await ctx.send(f"出た目: {choice}")

@commands.command(name="pon")
async def pon(ctx):
    gestures = [":cow: ✊", ":cow: :v:", ":cow: ✋"]
    random.seed()  # 乱数生成器を初期化する
    random_gesture = random.choice(gestures)
    await ctx.send(random_gesture)