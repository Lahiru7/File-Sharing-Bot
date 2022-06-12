#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○  Cʀᴇᴀᴛᴏʀ : <a href='tg://user?id={OWNER_ID}'>Tʜɪs Usᴇʀ</a>\n○ Lᴀɴɢᴜᴀɢᴇ : <code>Pʏᴛʜᴏɴ𝟹</code>\n○ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ ʏᴏᴜᴛᴜʙᴇ : <a href='https://www.youtube.com/channel/UCXQyTKOsTdy3aauIrCpGkhw'>Vɪᴇᴡ ᴄʜᴀɴɴᴇʟ</a>\n○  Cʜᴀɴɴᴇʟ : @MenakaLahiru7\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : @ADL_Drama</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❗️ 𝑪𝒍𝒐𝒔𝒆 ❗️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
