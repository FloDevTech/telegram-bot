# Telegram Bot

This project is a simple Telegram bot that responds to messages. It is built using the `python-telegram-bot` library.

## Project Structure

```
telegram-bot
├── src
│   ├── bot.py
│   └── handlers
│       └── message_handler.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot by talking to [BotFather](https://t.me/botfather) and obtain your bot token.

4. Update the bot token in `src/bot.py`.

## Usage

To run the bot, execute the following command:
```
python src/bot.py
```

The bot will start polling for messages and respond based on the defined message handling logic. 

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.