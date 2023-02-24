import hashlib
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to Akuma the Avatar Bot! Please send your name to generate your unique avatar.")
    keyboard = [[InlineKeyboardButton("Generate Avatar", callback_data='generate_avatar')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Click the button to generate your avatar!', reply_markup=reply_markup)

def generate_avatar(update, context):
    query = update.callback_query
    query.answer()
    name = query.message.text
    # Generate a unique hash based on the user's name
    unique_hash = hashlib.md5(name.encode('utf-8')).hexdigest()
    # Construct the URL of the avatar image
    avatar_url = f"https://www.gravatar.com/avatar/{unique_hash}?d=identicon"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=avatar_url)

def main():
    updater = Updater(token='5663162486:AAFq8WCTrJzzXoubmx1HMWaBjxGHGec4BDY', use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register callback handlers
    generate_avatar_handler = CallbackQueryHandler(generate_avatar, pattern='generate_avatar')
    dispatcher.add_handler(generate_avatar_handler)

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()