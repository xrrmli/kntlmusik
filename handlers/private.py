from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""saya adalah ramli musik bot, saya membiarkan anda memutar musik dalam grup obrolan anda  .

perintah yang digunakan:

/play - memainkan file audio atau YouTube video
/pause - menghentikan file audio
/resume - melanjutkan file audio kembali
/skip - melewati file audio
/mute - membisukan user yang kaya kontol
/unmute - membalikan user kontol yg udh tobat
/stop - membersihkan antrian dan menghapus anak kontol dari vcg
        """,
        reply_markup=InlineKeyboardMarkup(            [
            [
                [
                    InlineKeyboardButton(
                        "☠️ Tutorial", url="https://telegra.ph/%F0%9D%95%B4%F0%9D%96%91%F0%9D%96%92%F0%9D%96%97-04-03-2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/tongkrongannvirtual"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/painnhubbb"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Apakah anda ingin mencari video youtube?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya benar", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
