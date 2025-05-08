from flask import Flask, request
import telebot

# Siz bergan ma’lumotlar
BOT_TOKEN = '7714554918:AAHriVJ-tTmiUBbmABYJIaDnDiYDcejlMz4'
ADMIN_ID = 7098943602  # Sizning Telegram ID

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# Webhook orqali keladigan ma’lumotni qabul qilish
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    msg = (
        f"Yangi UC buyurtma:\n\n"
        f"UC: {data['uc']}\n"
        f"PUGB ID: {data['id']}\n"
        f"Nickname: {data['nick']}\n"
        f"Telegram: {data['user']}"
    )

    bot.send_message(ADMIN_ID, msg)
    return "OK", 200

# /start buyrug‘i bilan WebApp tugmasi
@bot.message_handler(commands=['start'])
def send_web_app(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    webAppInfo = telebot.types.WebAppInfo("https://starlit-faloodeh-e4975a.netlify.app")
    markup.add(telebot.types.KeyboardButton("UC Buyurtma berish", web_app=webAppInfo))
    bot.send_message(message.chat.id, "Quyidagi tugmani bosing:", reply_markup=markup)

# Flask serverni ishga tushurish (Render.com uchun)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
