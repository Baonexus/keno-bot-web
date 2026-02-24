import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot đã chạy OK!")

def start_bot():
    if not BOT_TOKEN:
        print("❌ Chưa cấu hình BOT_TOKEN")
        return

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot Telegram đang chạy...")
    app.run_polling()
