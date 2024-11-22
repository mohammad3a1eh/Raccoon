import json
import os
import module
import module.tbot
import feedparser
import asyncio


FILENAME = os.path.splitext(os.path.basename(__file__))[0]

NAME = "MediumRSSTag"
DESCRPTION = """
Written on 1403/07/06
"""

def load_(data, key):
    with open(f"./database/{data}.json", "r") as file:
        DATA_S = json.loads(file.read())
        
    with open(f"./values/{key}.txt", "r") as file:
        KEY_S = file.readlines()
        
    KEY_S = [line.strip() for line in KEY_S if line.strip()]
    
    return DATA_S, KEY_S


def read_rss(tag):
    url = f"https://medium.com/feed/tag/{tag}"
    feed = feedparser.parse(url)
    return feed


def post_exists_in_db(post, db):
    for item in db:
        if post['link'].split("?source=rss")[0] == item['link'].split("?source=rss")[0]:
            return True
    return False


def get_categories(entry):
    if hasattr(entry, 'tags'):
        categories = ' '.join([f"#{tag.term}".replace("-","_") for tag in entry.tags])
        return categories
    return ""


async def run(token, chat_id):
    db, tags = load_(data="medium", key=FILENAME)
    
    module.tbot.Telegram.init(token=token)
    await module.tbot.Telegram.send_text_to_tel(f"The raccoon script has started running the '{NAME}' module", chat_id=chat_id)
    
    post_ = 0
    
    for tag in tags:
        rss_feed = read_rss(tag)
        print(f"RSS feed for tag: {tag}")
        for entry in rss_feed.entries:
            
            if int(post_ / 5) == 0:
                await asyncio.sleep(15)
            else:
                await asyncio.sleep(10)

            post = {
                "link": f"{entry.link}",
            }
            
            if post_exists_in_db(post=post, db=db):
                continue
            
            post_ += 1

            title = entry.title
            author = entry.author if hasattr(entry, 'author') else "Unknown"
            categories = get_categories(entry)

            text = f"""
<b>{title}</b>(<i>{author}</i>)
<a href='{post['link']}'>Link</a>
{categories}"""

            module.tbot.Telegram.send_text_with_btn(text, post['link'], chat_id, token)
            
            db.append(post)

            with open(f"database/medium.json", "w") as file:
                json.dump(db, file, indent=4)

    await module.tbot.send_text_to_tel(f"Find {post_} post", chat_id)

