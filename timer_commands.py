# timer_commands.py

from discord.ext import commands
import asyncio

# タイマーの残り時間を管理するためのグローバル変数
remaining_time = 0

# タイマーが一時停止中かどうかを管理するためのグローバル変数
timer_paused = False
timer_task = None

@commands.command(
    name="start_timer",
    aliases=["set"]
)
async def start_timer(ctx: commands.Context, time_in_minutes: int):
    global remaining_time, timer_task, timer_paused
    if remaining_time > 0:
        await ctx.send("タイマーがすでに動作中です。リセットしてから再設定してください.")
        return

    remaining_time = time_in_minutes * 60
    timer_paused = False
    await ctx.send(f"{time_in_minutes} 分でタイマーをセットしました")

    # タイマータスクを作成
    timer_task = asyncio.create_task(timer_countdown(ctx))

@commands.command(
    name="end_timer",
    aliases=["end"]
)
async def end_timer(ctx: commands.Context):
    global timer_task, remaining_time
    if timer_task:
        timer_task.cancel()
        remaining_time = 0
        await ctx.send("タイマーが手動で終了しました")
    else:
        await ctx.send("タイマーは動作していません")

@commands.command(
    name="pause_timer",
    aliases=["pause", "p"]
)
async def pause_timer(ctx: commands.Context):
    global timer_paused
    if timer_task:
        timer_paused = not timer_paused  # 一時停止/再開を切り替え
        if timer_paused:
            await ctx.send("タイマーが一時停止しました。\n再開はもう一度 $p と入力してください")
        else:
            await ctx.send("タイマーが再開しました")
    else:
        await ctx.send("タイマーは動作していません")

@commands.command(
    name="check_time",
    aliases=["check", "ct"]
)
async def check_time(ctx: commands.Context):
    global remaining_time
    if remaining_time > 0:
        minutes = remaining_time // 60
        await ctx.send(f"残り時間: {minutes} 分")
    else:
        await ctx.send("タイマーは動作していません")

# タイマーのカウントダウン関数
async def timer_countdown(ctx):
    global remaining_time
    while remaining_time > 0:
        if not timer_paused:
            if remaining_time <= 300:
                minutes = remaining_time // 60
                if minutes == 5:
                    await ctx.send("のこり5分")
                elif minutes == 1:
                    await ctx.send("のこり1分")
                await asyncio.sleep(60)
                if not timer_paused:  # 一時停止中でない場合にのみ時間を減少
                    remaining_time -= 60
            else:
                await asyncio.sleep(60)
                if not timer_paused:  # 一時停止中でない場合にのみ時間を減少
                    remaining_time -= 60
        else:
            await asyncio.sleep(1)  # 1秒ごとに一時停止状態を確認
    if not timer_paused:  # タイマーが終了したら、一時停止中でない場合に終了メッセージを送信
        await ctx.send("終了!")
