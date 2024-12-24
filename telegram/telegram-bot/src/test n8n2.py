import requests
import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os
import whisper

#https://medium.com/@genaromateu/c%C3%B3mo-transcribir-un-audio-a-texto-en-python-con-los-servicios-de-azure-ff5af578f7f4

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    payload = dict(key1=update.message.text, key2='value2')
    print(payload)
    
    # development
    r = requests.get("http://localhost:5678/webhook-test/c5c1757f-bffd-41ed-8af9-72d8aec5409b",json=payload)

    #production
    # r = requests.get("http://localhost:5678/webhook/c5c1757f-bffd-41ed-8af9-72d8aec5409b",json=payload)

    # await update.message.reply_text(update.message.text)
async def echo_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    payload = dict(key1=update.message.audio, key2='value2')
    print(payload)
    
    # development
    r = requests.get("http://localhost:5678/webhook-test/c5c1757f-bffd-41ed-8af9-72d8aec5409b",json=payload)
async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    payload = dict(key1=update.message.voice.file_id, key2='value2')
    file_id = update.message.voice.file_id
    new_file =await update.message.effective_attachment.get_file()
    await new_file.download_to_drive('file_name.mp3')
    print(payload)
    
    files = {'upload_file': open('file_name.mp3','rb')}
    r = requests.post("http://localhost:5678/webhook-test/c5c1757f-bffd-41ed-8af9-72d8aec5409b",files=files)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7617555339:AAFF-A4XqpNGIEY_WcfrIX6hJibxdah_Jak").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.VOICE , echo_all))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
