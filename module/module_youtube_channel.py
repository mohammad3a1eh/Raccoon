import os
import json
import feedparser
import module.tbot
import asyncio
from urllib.parse import quote


FILENAME = os.path.splitext(os.path.basename(__file__))[0]

NAME = "YoutubeChannelUpload"
DESCRPTION = """
Written on 1403/08/10
"""

def load_(data, key):
    with open(f"./database/{data}.json", "r") as file:
        DATA_S = json.loads(file.read())

    with open(f"./values/{key}.txt", "r") as file:
        KEY_S = file.readlines()

    KEY_S = [line.strip() for line in KEY_S if line.strip()]

    return DATA_S, KEY_S


def read_rss(channel_id):
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(url)
    return feed


def post_exists_in_db(link, db):
    for item in db:
        if link['link'] == item['link']:
            return True
    return False


async def run(token, chat_id):
    db, channel_ids = load_(data="youtube", key=FILENAME)

    module.tbot.Telegram.init(token=token)
    await module.tbot.Telegram.send_text_to_tel(f"The raccoon script has started running the '{NAME}' module",chat_id=chat_id)

    video_ = 0

    for channel_id in channel_ids:
        rss_feed = read_rss(channel_id=channel_id)

        for entry in rss_feed.entries:

            if int(video_ / 5) == 0:
                await asyncio.sleep(15)
            else:
                await asyncio.sleep(10)

            video = {
                "link": entry.link
            }

            if post_exists_in_db(link=video, db=db):
                continue

            video_ += 1

            channel = entry.author
            title = entry.title

            text = f"""
<b>{title}</b>(<i>{channel}</i>)"""

            links = [
                [
                    {
                        "text": "youtube.com",
                        "url": f"{video['link']}"
                    }
                ]
            ]

            module.tbot.Telegram.send_text_with_btn(text, links, chat_id, token)

            db.append(video)

            with open(f"database/youtube.json", "w") as file:
                json.dump(db, file, indent=4)

    await module.tbot.Telegram.send_text_to_tel(f"Find {video_} video", chat_id)
