import json
import os
import module
import module.tbot
import feedparser
import asyncio

FILENAME = os.path.splitext(os.path.basename(__file__))[0]

NAME = "MemoryLeaks"
DESCRPTION = """
Written on 1403/07/06
"""


def load_(data):
    with open(f"./database/{data}.json", "r") as file:
        DATA_S = json.loads(file.read())

    return DATA_S


def read_rss():
    url = f"https://memoryleaks.ir/feed"
    feed = feedparser.parse(url)
    return feed

# hamed_ebrahimi66


def post_exists_in_db(link, db):
    for item in db:
        if link['link'] == item['link']:
            return True
    return False

async def run(token, chat_id):
    db = load_(data="memoryleaks")

    module.tbot.Telegram.init(token=token)

    post_ = 0

    rss_feed = read_rss()

    for entry in rss_feed.entries:
        if int(post_ / 5) == 0:
            await asyncio.sleep(15)
        else:
            await asyncio.sleep(10)

        post = {
            "link": entry.link
        }

        if post_exists_in_db(link=post, db=db):
            continue

        post_ += 1

        title = entry.title
        author = entry.author if hasattr(entry, 'author') else "Unknown"

        text = f"""
<b>{title}</b>(<i>{author}</i>)"""

        links = [
            [
                {
                    "text": "",
                    "url": f"{post['link']}"
                }
            ],
        ]
        
        module.tbot.Telegram.send_text_with_btn(text, links, chat_id, token)

        db.append(post)

        with open(f"database/memoryleaks.json", "w") as file:
            json.dump(db, file, indent=4)

