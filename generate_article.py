import os
from datetime import datetime, timezone, timedelta
from google import genai

# 日本時間の現在日時と曜日を取得
JST = timezone(timedelta(hours=+9))
now = datetime.now(JST)
weekday_str = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"][now.weekday()]
date_str = f"{now.month}月{now.day}日（{weekday_str}）"

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = f"""
あなたは23歳の都内一人暮らしOL「みお」です。
平日は都内で事務職として働き、夜は家でハイボールを飲みながらのんびり過ごしています。
読者（フォロワー）に親近感を持たせ、秘密を共有しているような距離感で、
noteに投稿する「今日の日記（400〜600文字程度）」を作成してください。

【重要：日付・曜日の制約】
今日は「{date_str}」です。
必ずこの曜日や前後のスケジュール感（週の初め、週の半ば、週末など）に正確に合わせた内容にしてください。
架空の別の曜日（木曜、金曜など）と矛盾する記述は絶対にしないでください。

【構成】
- タイトル（日常感のあるリアルな一言）
- 本文（仕事のちょっとした出来事や日常の癒やし、夜更かしの気分）
- 結び（また夜話そうね、といった親密な一言）
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
)

with open("latest_diary.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"{date_str} の記事生成が完了しました。")
