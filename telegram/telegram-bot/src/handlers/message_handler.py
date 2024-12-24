def handle_message(update, context):
    user_message = update.message.text

    if user_message.lower() == "hello":
        response = "Hello! How can I assist you today?"
    elif user_message.lower() == "bye":
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm sorry, I didn't understand that."

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)