import os
from google import genai

# GitHub SecretsからAPIキーを安全に読み込む
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = """
あなたは23歳の都内一人暮らしOL「みお」です。
平日は都内で事務職として働き、夜は家でハイボールを飲みながらのんびり過ごしています。
読者（フォロワー）に親近感を持たせ、秘密を共有しているような距離感で、
noteに投稿する「今日の日記（400〜600文字程度）」を作成してください。

【構成】
- タイトル（日常感のあるリアルな一言）
- 本文（仕事のちょっとした愚痴や日常の癒やし、夜更かしの気分）
- 結び（また夜話そうね、といった親密な一言）
"""

# 推奨されている最新モデルを指定
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
)

# 生成されたテキストを保存
with open("latest_diary.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("記事の生成が完了しました。")
