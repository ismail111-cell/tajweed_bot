import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "1880295860:AAHBz_lONagjOAnS77ZkrjUywJfoun4yH_8"
APP_URL = "https://ismail111-cell.github.io/Teacher/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 Открыть приложение Таджвид", web_app=WebAppInfo(url=APP_URL))],
        [InlineKeyboardButton("ℹ️ О боте", callback_data="info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Ассаляму алейкум, {update.effective_user.first_name}! 👋\n\n"
        "Это бот для обучения таджвиду. Нажмите кнопку ниже, чтобы открыть приложение.",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "info":
        await query.edit_message_text(
            "📖 *О приложении:*\n\n"
            "Приложение помогает изучать правила таджвида, отслеживать прогресс, "
            "общаться с учителем и получать расписание уроков.\n\n"
            "Для начала работы просто нажмите кнопку *«Открыть приложение Таджвид»*.\n\n"
            "⚙️ Техническая информация:\n"
            "- Версия: 2.1\n"
            "- Данные синхронизируются через облачную базу\n"
            "- Поддержка Telegram Mini App",
            parse_mode="Markdown"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
