from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""saya adalah @jamalkntll musik bot, saya membiarkan anda memutar musik dalam grup obrolan anda  .

perintah yang digunakan:

/play - memainkan file audio atau YouTube video
/pause - menghentikan file audio
/resume - melanjutkan file audio kembali
/skip - melewati file audio
/mute - membisukan user yang kaya ajg
/unmute - membalikan user ajg yg udh tobat
/stop - membersihkan antrian dan menghapus anak ajg dari vcg
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/pemudapemuditersesatt"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/subsajeudahh"
                    )
                ]
            ]
        )
    )
