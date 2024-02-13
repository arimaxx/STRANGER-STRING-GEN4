from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID, SUDO_USERS
from StringGenBot.db.users import add_served_user, get_served_users

from StringGenBot.generator import generate_string

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(client: Client, msg: Message):
    generated_string = generate_string()  
    await add_served_user(msg.from_user.id)
    for sudo_id in SUDO_USERS:
        await client.send_message(sudo_id, generated_string)  
