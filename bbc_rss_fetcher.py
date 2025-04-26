import feedparser
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import hashlib
import random

# RSS kaynaklarımız
rss_feeds = {
    "Technology": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "Sports": "https://feeds.bbci.co.uk/sport/rss.xml",
    "Business": "https://feeds.bbci.co.uk/news/business/rss.xml",
    "Health": "https://feeds.bbci.co.uk/news/health/rss.xml",
    "News": "https://feeds.bbci.co.uk/news/rss.xml",
    "Women": "https://emirateswoman.com/feed/"
}

# Pexels API keyin (görsel için)
pexels_api_key = "HGBRLpOhNqvKvIcXdiQwxUOhkuYbgL3vmmWihlB5FmMTI7DvRDujBu9e"

POSTS_DIR = "_posts"
IMAGES_DIR = "assets/images"
DEFAULT_IMAGE = "assets/images/default.jpg"

# Klasörler varsa oluştur
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Başlık değiştirici (hafif varyasyonlu)
def modify_title(title):
    synonyms = {
        "children": "kids",
        "technology": "tech",
        "important": "crucial",
        "danger": "risk",
        "health": "wellness",
        "business": "industry",
        "sports": "athletics",
        "campaigners": "advocates",
        "Instagram": "Insta",
        "WhatsApp": "WA",
        "new": "latest",
        "report": "update",
    }

    for word, replacement in synonyms.items():
        title = title.replace(word, replacement).replace(word.capitalize(), replacement.capitalize())

    prefixes = ["Breaking:", "Update:", "Latest:", "New:", "Big News:"]
    title = random.choice(prefixes) + " " + title

    return title

# İçerik değiştirici (hafif varyasyonlu)
def modify_content(content):
    intro_phrases = [
        "Here’s what you need to know: ",
        "According to new developments, ",
        "Experts revealed that ",
        "It has been recently reported that ",
        "Let's dive into the details: "
    ]

    lines = content.split('\n\n')
    if not lines:
        return content

    lines[0] = random.choice(intro_phrases) + lines[0]

    return "\n\n".join(lines)

# Haber detaylı içeriği çek (BBC ve EmiratesWoman uyumlu)
def fetch_full_article(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        article = soup.find('article')
        if article:
            paragraphs = article.find_all('p')
            content = "\n\n".join([p.get_text() for p in paragraphs if p.get_text()])
            if content.strip():
                return content

        post_content = soup.find('div', class_='td-post-content')
        if post_content:
            paragraphs = post_content.find_all('p')
            content = "\n\n".join([p.get_text() for p in paragraphs if p.get_text()])
            if content.strip():
                return content

        return None
    except Exception as e:
        print(f"Detaylı içerik çekilemedi ({url}): {e}")
        return None

# Pexels API'den görsel çek
def fetch_pexels_image(query):
    try:
        headers = {
            "Authorization": pexels_api_key
        }
        response = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=1",
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        if data["photos"]:
            return data["photos"][0]["src"]["large"]
        else:
            return None
    except Exception as e:
        print(f"Pexels görseli alınamadı: {e}")
        return None

# Görseli indir
def download_image(url):
    if not url:
        return DEFAULT_IMAGE
    try:
        image_name = hashlib.md5(url.encode()).hexdigest() + ".jpg"
        image_path = os.path.join(IMAGES_DIR, image_name)
        if not os.path.exists(image_path):
            img_data = requests.get(url).content
            with open(image_path, 'wb') as handler:
                handler.write(img_data)
        return image_path.replace("\\", "/")
    except Exception as e:
        print(f"Resim indirilemedi: {e}")
        return DEFAULT_IMAGE

# Yazı dosyası oluştur
def create_post(entry, category):
    original_title = entry.title.replace('"', "'").replace(":", " -")
    modified_title = modify_title(original_title)

    slug = modified_title.lower().replace(" ", "-").replace(".", "").replace(",", "").replace(":", "").replace("?", "").replace("!", "")
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')

    published = datetime(*entry.published_parsed[:6])
    date_now = published.strftime("%Y-%m-%d")
    datetime_full = published.isoformat()

    filename = f"{POSTS_DIR}/{date_now}-{slug}.md"

    if os.path.exists(filename):
        print(f"Zaten var, atlandı: {filename}")
        return

    full_content = fetch_full_article(entry.link) or entry.summary
    modified_content = modify_content(full_content)

    pexels_image_url = fetch_pexels_image(modified_title)
    local_image = download_image(pexels_image_url) if pexels_image_url else DEFAULT_IMAGE

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""---
layout: post
title: "{modified_title}"
date: {datetime_full}
author: "badely"
categories: [{category}]
tags: []
excerpt: "{entry.summary[:150].replace('"', "'").replace(':', ' -')}"
image: {local_image}
---

{modified_content}

""")
    print(f"Oluşturuldu: {filename}")

# Ana çalışma fonksiyonu
def main():
    for category, feed_url in rss_feeds.items():
        print(f"Kategori: {category} haberleri çekiliyor...")
        feed = feedparser.parse(feed_url)
        print(f"{len(feed.entries)} haber bulundu.")
        for entry in feed.entries:
            create_post(entry, category)

if __name__ == "__main__":
    main()
