import feedparser
import argparse
import sys
import telegram
import re
import json
import asyncio
import time


with open("DB.json", "r") as file:
    db = json.loads(file.read())

parser = argparse.ArgumentParser(description='Send RSS feed updates to Telegram bot.')
parser.add_argument('--telegram_token', type=str, required=True, help='Your Telegram bot token')
parser.add_argument('--chat_id', type=str, required=True, help='Your Telegram chat ID')
args = parser.parse_args()


if not args.telegram_token:
    print("Error: Telegram bot token is required.")
    sys.exit(1)


if not args.chat_id:
    print("Error: Telegram chat ID is required.")
    sys.exit(1)


telegram_token = args.telegram_token
chat_id = args.chat_id
bot = telegram.Bot(token=telegram_token)


tags = [
    "idor",
    "xss",
    "cybersecurity",
    "python",
    "infosec"
]


def read_rss(tag):
    url = f"https://medium.com/feed/tag/{tag}"
    feed = feedparser.parse(url)
    return feed


async def send_text_to_tel(text, chat_id):
    await bot.send_message(
        chat_id=chat_id,
        text=text
    )
    
    
async def send_image_to_tel(text, chat_id, image_url):
    await bot.send_photo(
        photo=image_url, 
        caption=text,
        chat_id=chat_id,
    )
    
    
def post_exists_in_db(post, db):
    for item in db:
        if post['link'] == item['link']:
            return True
    return False


def get_categories(entry):
    if hasattr(entry, 'tags'):
        categories = ' '.join([f"#{tag.term}".replace("-","_") for tag in entry.tags])
        return categories
    return ""


async def main():
    await send_text_to_tel("Start the process", chat_id)

    for tag in tags:
        rss_feed = read_rss(tag)
        print(f"RSS feed for tag: {tag}")
        for entry in rss_feed.entries:
            
            time.sleep(8)
            
            post = {
                "title" : f"{entry.title}",
                "summary" : f"{entry.summary}",
                "link" : f"{entry.link}",
                "published" : f"{entry.published}" 
            }
            
            if post_exists_in_db(post=post, db=db):
                continue
            
            author = entry.author if hasattr(entry, 'author') else "Unknown"
            categories = get_categories(entry)
            
            text = f"""
**{post['title']}**
-> {author}

{post['link']}

{post['published']}
-------------------
bot_tag #{tag}
medium_tag {categories}
            """
            
            img_src = re.search(r'<img src="([^"]+)"', post["summary"])
            
            if img_src:
                image_url = img_src.group(1)
                await send_image_to_tel(text, chat_id, image_url)
            else:
                await send_text_to_tel(text, chat_id)
            
            db.append(post)

            with open("DB.json", "w") as file:
                json.dump(db, file, indent=4)

# اجرای برنامه
if __name__ == "__main__":
    asyncio.run(main())
