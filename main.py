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
    if num >= 11:
        return "TÀI"
    else:
        return "XỈU"

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()

    try:
        kq = decode_mb5(code)
        tx = tai_xiu(kq)

        await update.message.reply_text(
            f"🤖 TOOL AI TÀI XỈU\n\n"
            f"Mã: {code}\n"
            f"Kết quả số: {kq}\n"
            f"Kết luận: {tx}"
        )
    except:
        await update.message.reply_text("❌ Mã không hợp lệ")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("BOT TOOL AI TÀI XỈU đang chạy...")

app.run_polling()
