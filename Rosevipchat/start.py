from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from EsproAiChat.Espro import app  # import bot from module

# ===== /start Command Handler =====
@app.on_message(filters.private & filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Chat with AI 🤖", callback_data="chat")],
            [InlineKeyboardButton("Help ❓", callback_data="help")]
        ]
    )

    await message.reply(
        "💠 Welcome to Espro AI Chat!\n\n"
        "Click below to start chatting or get help.",
        reply_markup=keyboard
    )

# ===== Callback Query Handler =====
@app.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data
    if data == "chat":
        await callback_query.message.edit_text(
            "✅ You can now type your message and I will reply as a friendly AI! 😄"
        )
    elif data == "help":
        await callback_query.message.edit_text(
            "❗ Help:\n"
            "- Type any message and I will reply in a friendly, short 1-line format.\n"
            "- Playful emojis included 😜\n"
            "- /start to show this menu again."
        )

# ===== Run Bot =====
if __name__ == "__main__":
    print("🤖 Espro AI Chat Bot (with Start Button) is running...")
    app.run()
