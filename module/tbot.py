import telegram
# import asyncio

class Telegram:
    bot = None

    @classmethod
    def init(cls, token):
        cls.bot = telegram.Bot(token=token)

    @classmethod
    async def send_text_to_tel(cls, text, chat_id):
        if cls.bot is None:
            raise ValueError("Bot not initialized. Call Telegram.init(token) first.")
        
        await cls.bot.send_message(
            chat_id=chat_id,
            text=text
        )

    @classmethod
    async def send_image_to_tel(cls, text, chat_id, image_url):
        if cls.bot is None:
            raise ValueError("Bot not initialized. Call Telegram.init(token) first.")
        
        
        await cls.bot.send_photo(
            chat_id=chat_id,
            photo=image_url,
            caption=text
        )


Telegram.init('your-telegram-token')


# async def main():
#     await Telegram.send_text_to_tel('Hello!', 'your-chat-id')
#     await Telegram.send_image_to_tel('Check this image', 'your-chat-id', 'https://image-url.com/image.jpg')


# asyncio.run(main())
