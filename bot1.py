# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: CallbackContext) -> None:
    """Handler for the /start command with URL buttons"""
    # Create inline keyboard buttons with direct URLs
    keyboard = [
        [
            InlineKeyboardButton("FoFNews Channel", url="https://t.me/FoFNews"),
            InlineKeyboardButton("Trust Test Bot", url="http://t.me/trust_Test88_Bot/Trusts"),
            InlineKeyboardButton("X.com", url="https://x.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Path to your welcome image (make sure this path is correct)
    welcome_image_path = 'welcome_image.jpg'
    
    try:
        # Open the image file
        with open(welcome_image_path, 'rb') as image_file:
            # Send the image with caption and inline buttons
            await update.message.reply_photo(
                photo=image_file,
                caption="Welcome to our Telegram Bot! 🚀\n\n"
                        "Discover our channels and resources:\n\n"
                        "• FoFNews: Stay updated with the latest news\n"
                        "• Trust Test Bot: Explore our trusted services\n"
                        "• X.com: Visit our main platform\n\n"
                        "Click the buttons below to explore!",
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        # Fallback if image is not found
        await update.message.reply_text(
            "Welcome to our Telegram Bot! 🚀\n\n"
            "Discover our channels and resources:\n\n"
            "• FoFNews: Stay updated with the latest news\n"
            "• Trust Test Bot: Explore our trusted services\n"
            "• X.com: Visit our main platform\n\n"
            "Click the buttons below to explore!",
            reply_markup=reply_markup
        )


async def handle_image(update: Update, context: CallbackContext) -> None:
    """Handler for image messages"""
    # Get the largest photo (highest resolution)
    photo = update.message.photo[-1]
    
    # Create inline keyboard buttons with direct URLs
    keyboard = [
        [
            InlineKeyboardButton("FoFNews Channel", url="https://t.me/FoFNews"),
            InlineKeyboardButton("Trust Test Bot", url="http://t.me/trust_Test88_Bot/Trusts"),
            InlineKeyboardButton("X.com", url="https://x.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send response with buttons
    await update.message.reply_text(
        "Welcome to our Telegram Bot! 🚀\n\n"
        "Discover our channels and resources:\n\n"
        "• FoFNews: Stay updated with the latest news\n"
        "• Trust Test Bot: Explore our trusted services\n"
        "• X.com: Visit our main platform\n\n"
        "Click the buttons below to explore!",
        reply_markup=reply_markup
    )


def main() -> None:
    """Main function to start the bot"""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))
    
    # Start the Bot
    application.run_polling(drop_pending_updates=True)


if __name__ == '__main__':
    main()