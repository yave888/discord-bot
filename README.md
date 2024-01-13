# マーダーミステリー Discord Bot

## 概要
この Discord Bot はマーダーミステリーの進行やタイマー、コマンドを補助するための機能を提供します。

## 実装コマンド
- **check_time (ct):** 残り時間確認
- **dice (roll):** サイコロを振ります
- **end_timer (end):** タイマーを手動で終了します
- **pause_timer (p):** タイマーの一時停止/再開を切り替えます
- **pon:** じゃんけんの手をランダムで返します
- **start_timer (set):** タイマーを開始します
- **h:** ヘルプを表示します
  - ()のあるものは省略して入力可能 (例. $ct $p)

## Bot 実装方法
1. プロジェクトをクローンまたはダウンロードします。
2. `config.py` ファイルをプロジェクトのルートに作成します。このファイルには Discord Bot のトークンを保存します。
    ```python
    # config.py

    TOKEN = "Your-Bot-Token-Here"
    ```
3. `gitignore` ファイルに `config.py` を追加し、トークンを安全に保護します。
    ```
    # .gitignore

    config.py
    ```
4. Bot の実行には Python 3.x が必要です。以下のコマンドで依存関係をインストールします。
    ```bash
    pip install -r requirements.txt
    ```
5. `main.py` を実行して Bot を起動します。
    ```bash
    python main.py
    ```
6. Bot は Discord 上で指定したコマンドに反応し、機能を提供します。

**注意:** プロジェクトには `.gitignore` が含まれています。`.gitignore` ファイルは `config.py` を Git リポジトリに含めないようにしています。トークンが漏洩しないように十分に注意してください。
