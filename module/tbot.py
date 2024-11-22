import telegram
import requests


class Telegram:
    bot = None

    @classmethod
    def init(cls, token):
        cls.bot = telegram.Bot(token=token)

    @classmethod
    async def send_text_to_tel(cls, text, chat_id):
        if cls.bot is None:
            raise ValueError("Bot not initialized. Call Telegram.init(token) first.")
        await cls.bot.send_message(chat_id=chat_id, text=text)

    @classmethod
    def send_text_with_btn(cls, text, link, chat_id, bot_token):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "reply_markup": {
                "inline_keyboard": [
                    [
                        {
                            "text": "medium.com",
                            "url": f"{link}"
                        }
                    ],
                    [
                        {
                            "text": "freedium.cfd",
                            "url": f"https://freedium.cfd/{link}"
                        }
                    ]
                ]
            }
        }

        response = requests.post(url, json=payload)

    @classmethod
    async def send_image_to_tel(cls, text, chat_id, image_url):
        if cls.bot is None:
            raise ValueError("Bot not initialized. Call Telegram.init(token) first.")
        await cls.bot.send_photo(chat_id=chat_id, photo=image_url, caption=text)

    @classmethod
    def send_audio_to_tel(cls, file_path, caption, link, chat_id, bot_token):
        url = f"https://api.telegram.org/bot{bot_token}/sendAudio"
        files = {'audio': open(file_path, 'rb')}
        data = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": "HTML",
            "reply_markup": {
                "inline_keyboard": [
                    [
                        {
                            "text": "youtube.com",
                            "url": {link}
                        }
                    ]
                ]
            }
        }

        response = requests.post(url, files=files, data=data)


