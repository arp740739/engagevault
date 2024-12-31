import asyncio
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "🌟 *Welcome to EngageVault!* 🌟\n\n"
        "📱 *What is EngageVault?*\n"
        "We help you to boost your social media engagement through our unique point-based system.\n\n"
        "🎯 *How it works:*\n"
        "• Complete social tasks (likes, shares, comments, follows)\n"
        "• Earn points for each completed task\n"
        "• Use your points to enhance your social media presence\n\n"
        "🚀 *Benefits:*\n"
        "• Increased engagement rate\n"
        "• Organic growth\n"
        "• Genuine interactions\n"
        "• Active community building\n\n"
        "⭐️ *Early Bird Advantages:*\n"
        "• Priority access to new features\n"
        "• Bonus point multipliers\n"
        "• Guaranteed airdrop allocation\n"
        "• Exclusive early adopter badge\n\n"
        "🔥 *Don't miss out!* Early adoption is your greatest advantage. Join now to secure your position as an early user!\n\n"
        "Ready to enhance your social presence? Click the button below! 👇"
    )
    
    web_app_url = os.getenv('WEBAPP_URL')
    
    # Création du bouton inline
    keyboard = [[
        InlineKeyboardButton(
            "🚀 Launch EngageVault",
            web_app=WebAppInfo(url=web_app_url)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Envoyer le message avec le bouton directement attaché
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

def run_bot():
    application = Application.builder().token(os.getenv('BOT_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot démarré ! Utilisez Ctrl+C pour arrêter.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    run_bot()