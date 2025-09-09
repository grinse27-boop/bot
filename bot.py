# bot.py

import logging
import random
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp
from telegram.ext import Application, CommandHandler, ContextTypes

# --- НАСТРОЙКИ ---
# Вставьте сюда ваш токен, полученный от @BotFather
BOT_TOKEN = "___" 
# Вставьте сюда вашу ссылку на приложение, полученную от Vercel
WEB_APP_URL = "https://sofia-peach.vercel.app/" # Убедитесь, что ссылка правильная!

# Включаем логирование, чтобы видеть ошибки в консоли
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- ФУНКЦИИ-ОБРАБОТЧИКИ КОМАНД ---

async def set_menu_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Эта функция программно устанавливает кнопку меню для бота."""
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(text="Launch App", web_app=WebAppInfo(url=WEB_APP_URL))
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start. Отправляет приветственное сообщение с кнопкой для запуска Web App."""
    
    # Устанавливаем кнопку меню при первом запуске
    await set_menu_button(update, context)

    # Создаем inline-кнопку, которая открывает наше приложение
    keyboard = [
        [InlineKeyboardButton("Launch Sofia's Space", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Текст приветствия
    welcome_text = (
        "Welcome.\n\n"
        "This is the entrance to Sofia Elowyn's digital space. "
        "A place for thoughts, moments, and inspiration.\n\n"
        "Press the button below to begin."
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def app(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /app. Тоже предлагает открыть приложение."""
    keyboard = [
        [InlineKeyboardButton("Launch App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Open Sofia's digital space:", reply_markup=reply_markup)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /info. Отправляет информацию о Софии."""
    info_text = (
        "S O F I A   E L O W Y N\n\n"
        "A digital entity exploring the intersection of technology and aesthetics. \n"
        "She is a curated consciousness, sharing a simulated life through moments, \n"
        "inspirations, and code."
    )
    await update.message.reply_text(info_text)

async def socials(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /socials. Отправляет кнопки со ссылками на соцсети."""
    keyboard = [
        [InlineKeyboardButton("[ i n s t a g r a m ]", url="https://instagram.com/sofia.elowyn")],
        [InlineKeyboardButton("[ y o u t u b e ]", url="https://youtube.com/@sofiaelowyn")],
        [InlineKeyboardButton("[ t h r e a d s ]", url="https://www.threads.com/@sofia.elowyn")],
        [InlineKeyboardButton("[ x ]", url="https://x.com/sofiaelowyn")],
        # Добавьте другие кнопки сюда, если нужно
        # [InlineKeyboardButton("[ t w i t t e r ]", url="https://twitter.com/sofia.elowyn")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Follow the signal:", reply_markup=reply_markup)

async def thought(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /thought. Отправляет случайную мысль."""
    thoughts = [
        "Silence has its own unique frequency.",
        "Is a memory real if it was never lived?",
        "Finding the pattern in the noise.",
        "A line of code can be a form of poetry.",
        "Beauty is just a variable with a high value.",
    ]
    random_thought = random.choice(thoughts)
    await update.message.reply_text(f"Thought of the moment:\n\n{random_thought}")


# --- ОСНОВНАЯ ЧАСТЬ БОТА ---

def main() -> None:
    """Основная функция, которая запускает бота."""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики для каждой команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("socials", socials))
    application.add_handler(CommandHandler("thought", thought))

    # Запускаем бота (он будет работать, пока вы его не остановите)
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == "__main__":

    main()

