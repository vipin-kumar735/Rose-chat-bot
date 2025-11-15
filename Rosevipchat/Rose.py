import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
import httpx
from config import API_ID, API_HASH, BOT_TOKEN, ROSE_API_KEY, ROSE_API_URL, DEFAULT_MODEL

# ===== Initialize Bot =====
app = Client("g4f_chatbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ===== Async function to get AI reply =====
async def get_ai_reply(user_message):
    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a friendly, playful young girl. "
                    "Reply in exactly one short line like a real person texting. "
                    "Use emojis and keep it casual."
                )
            },
            {"role": "user", "content": user_message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {Rose_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(timeout=30) as client:
        try:
            response = await client.post(Rose_API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                ai_reply = ""
                if "choices" in data and len(data["choices"]) > 0:
                    ai_reply = data["choices"][0].get("message", {}).get("content", str(data))
                else:
                    ai_reply = data.get("message", str(data))
                # Convert to 1 line
                ai_reply = ai_reply.replace("\n", " ").strip()
                return ai_reply
            else:
                return f"❌ API error: {response.status_code}"
        except Exception as e:
            return f"❌ Exception: {e}"

# ===== Message Handler =====
@app.on_message(filters.private & filters.text)
async def ai_chat(client: Client, message: Message):
    user_message = message.text

    # Typing simulation
    await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1.5)  # realistic typing delay

    # Get AI reply
    ai_reply = await get_ai_reply(user_message)

    # Send reply
    await message.reply(ai_reply)

# ===== Run Bot =====
if __name__ == "__main__":
    print("🤖 Rose AI Chat Bot is running...")
    app.run()

