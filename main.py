import os
import hashlib
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

def decode_mb5(code):
    h = hashlib.md5(code.encode()).hexdigest()
    num = int(h, 16)
    result = num % 18 + 1
    return result

def tai_xiu(num):
    return "TÀI" if num >= 11 else "XỈU"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    kq = decode_mb5(code)
    tx = tai_xiu(kq)

    await update.message.reply_text(
        f"🤖 TOOL AI TÀI XỈU\n\n"
        f"Mã: {code}\n"
        f"Kết luận: {tx}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("TOOL AI TÀI XỈU đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
