# help_command.py

from discord.ext import commands

@commands.command(name="h")
async def custom_help(ctx):
    help_text = (
        "実装コマンド\n"
        "- check_time (ct): 残り時間確認\n"
        "- dice: サイコロを振ります\n"
        "- end_timer (end): タイマーを手動で終了します\n"
        "- pause_timer (p): タイマーの一時停止/再開を切り替えます\n"
        "- pon: じゃんけんの手をランダムで返します\n"
        "- start_timer (set): タイマーを開始します\n"
        "- h: ヘルプを表示します\n"
        "()のあるものは省略して入力可"
        "例. $ct $p"
    )
    await ctx.send(help_text)
