import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("BOT TÀI XỈU\n\nGửi MD5 để phân tích.")

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.strip()

    try:
        value = int(text,16)

        mod = value % 18

        if mod >= 11:
            result = "TÀI"
        else:
            result = "XỈU"

        percent = random.randint(60,90)

        await update.message.reply_text(
            f"Dự đoán: {result}\nTỷ lệ: {percent}%"
        )

    except:
        await update.message.reply_text("MD5 không hợp lệ")

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, analyze))

    print("Bot đang chạy...")

    app.run_polling()

if __name__ == "__main__":
    main()
