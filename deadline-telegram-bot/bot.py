import logging
from datetime import datetime, timezone

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.constants import ParseMode
import pytz

import config


HELP_MESSAGE = """
⚪ /ccs - Show CCS Deadline
⚪ /help – Show help
"""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=HELP_MESSAGE, parse_mode=ParseMode.HTML
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=HELP_MESSAGE, parse_mode=ParseMode.HTML
    )

async def ccs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now_time = datetime.now(tz=pytz.timezone(config.time_zone))
    ccs_deadline = datetime(2023, 5, 4, 23, 59, 00, tzinfo=pytz.timezone('Etc/GMT+12'))
    time_delta = ccs_deadline - now_time
    days = time_delta.days
    hours = time_delta.seconds // 3600
    minutes = (time_delta.seconds // 60) % 60
    seconds = time_delta.seconds % 60
    deadline_str = f"距离 CCS deadline 还有 <b>{days} 天, {hours} 小时, {minutes} 分钟, {seconds} 秒</b>"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=deadline_str, parse_mode=ParseMode.HTML
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(config.telegram_bot_token).build()


    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    ccs_handler = CommandHandler("ccs", ccs)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(ccs_handler)
    application.run_polling()
