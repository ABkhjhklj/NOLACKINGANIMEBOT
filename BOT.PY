from telegram import Bot
from openai import OpenAI
import time

BOT_TOKEN = "8388130267:AAGzhuxXJTbDIS4BiBKMxPIDxc4kORkL_Ho"
CHANNEL = "@AABEL_BOT"
OPENAI_KEY = os.getenv("OPENAI_KEY")
bot = Bot(token=BOT_TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Write a dark anime fact in a cold, intimidating style. 30 to 60 words. No emojis."}
        ]
    )

    text = response.choices[0].message.content
    bot.send_message(chat_id=CHANNEL, text=text)

    time.sleep(3600)
