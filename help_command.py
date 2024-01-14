# help_command.py

from discord.ext import commands

@commands.command(name="h")
async def custom_help(ctx):
    help_text = (
        "## 実装コマンド\n"
        "- **`$check_time` (`$ct`):** 残り時間確認\n"
        "- **`$dice` (`$roll`):** サイコロを振ります\n"
        "  - $dice 30 などと打つと1～30の乱数を返す\n"
        "- **`$end_timer` (`$end`):** タイマーを手動で終了します\n"
        "- **`$pause_timer` (`$p`):** タイマーの一時停止/再開を切り替えます\n"
        "- **`$pon`:** じゃんけんの手をランダムで返します\n"
        "- **`$start_timer` (`$set`):** タイマーを開始します\n"
        "- **`$h`:** ヘルプを表示します\n"
        "  - ()のあるものは省略して入力可能 (例. `$ct` `$p`)\n"
        "- タイマーをセットする際は時間も一緒に入力してください\n"
        "  - 15分でタイマーをセットする場合 `$set 15`"
    )
    await ctx.send(help_text)
