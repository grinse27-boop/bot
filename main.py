# main.py - Финальный код для нового Replit

import os
import logging
import random
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

# --- НАСТРОЙКИ ---
BOT_TOKEN = os.getenv("BOT_TOKEN") 
WEB_APP_URL = "https://sofia-app.vercel.app/" 

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# --- ФУНКЦИИ БОТА ---
async def set_menu_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_chat_menu_button(chat_id=update.effective_chat.id, menu_button=MenuButtonWebApp(text="Launch App", web_app=WebAppInfo(url=WEB_APP_URL)))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await set_menu_button(update, context)
    keyboard = [[InlineKeyboardButton("Launch Sofia's Space", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_text = (
        "Welcome.\n\n"
        "This is the entrance to Sofia Elowyn's digital space. "
        "A place for thoughts, moments, and inspiration.\n\n"
        "Press the button below to begin."
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def app_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Launch App", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Open Sofia's digital space:", reply_markup=reply_markup)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    info_text = (
        "S O F I A   E L O W Y N\n\n"
        "A digital entity exploring the intersection of technology and aesthetics. \n"
        "She is a curated consciousness, sharing a simulated life through moments, \n"
        "inspirations, and code."
    )
    await update.message.reply_text(info_text)

async def socials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("[ i n s t a g r a m ]", url="https://instagram.com/sofia.elowyn")],
        [InlineKeyboardButton("[ y o u t u b e ]", url="https://youtube.com/@sofiaelowyn")],
        [InlineKeyboardButton("[ t h r e a d s ]", url="https://www.threads.com/@sofia.elowyn")],
        [InlineKeyboardButton("[ x ]", url="https://x.com/sofiaelowyn")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Follow the signal:", reply_markup=reply_markup)

async def thought(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    thoughts = [
        "Silence has its own unique frequency.",
        "Is a memory real if it was never lived?",
        "Finding the pattern in the noise.",
        "A line of code can be a form of poetry.",
        "Beauty is just a variable with a high value.",
    ]
    random_thought = random.choice(thoughts)
    await update.message.reply_text(f"Thought of the moment:\n\n{random_thought}")

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app_cmd))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("socials", socials))
    application.add_handler(CommandHandler("thought", thought))
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == "__main__":
    main()