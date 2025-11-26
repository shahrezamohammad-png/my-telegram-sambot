import telebot
from google import generativeai as genai
#tanzim API
TELEGRAM_TOKEN="8453278691:AAF9So3a3rgogn05HSggbl_XPdr-4SaW9I4"
#tanzim gemini
GEMINI_API_KEY="AIzaSyBtQdu_LTMSuqoemAHRi9ELgcDfOlq3f8g"

#rah andazi
bot= telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

# ایجاد مدل Gemini
model = genai.GenerativeModel('gemini-pro')

# تابعی برای پاسخ به تمام پیام‌ها
@bot.message_handler(func=lambda message: True)
def send_gemini_response(message):
    try:
        # نشان دادن وضعیت "در حال تایپ"
        bot.send_chat_action(message.chat.id, 'typing')
        
        # تولید پاسخ با Gemini
        response = model.generate_content(message.text)
        
        # ارسال پاسخ به کاربر
        bot.reply_to(message, response.text)
        
    except Exception as e:
        bot.reply_to(message, "متأسفانه خطایی رخ داد! لطفاً دوباره تلاش کنید.")

# اجرای ربات
print("ربات در حال اجراست...")
bot.polling()