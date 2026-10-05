"""
Starter updater.
Replace/extend FEEDS with the RSS feeds you have permission to use.
This starter safely collects headlines into daily_update.json.
To turn headlines into 50 high-quality MCQs, connect a question-generation API
using a GitHub Actions secret and validate the output before publishing.
"""
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from datetime import date
import json

FEEDS = [
    # Add trusted RSS endpoints here.
]

def read_feed(url):
    req = Request(url, headers={"User-Agent":"MPSC-Daily-Updater/1.0"})
    xml = urlopen(req, timeout=20).read()
    root = ET.fromstring(xml)
    out=[]
    for item in root.findall(".//item")[:20]:
        title=(item.findtext("title") or "").strip()
        link=(item.findtext("link") or "").strip()
        desc=(item.findtext("description") or "").strip()
        if title: out.append({"category":"Current Affairs","title":title,"summary":desc,"url":link})
    return out

path="daily_update.json"
try:
    with open(path,encoding="utf-8") as f: data=json.load(f)
except Exception:
    data={"daily":[],"news":[],"pyq":[],"gk":[]}

news=[]
for feed in FEEDS:
    try: news.extend(read_feed(feed))
    except Exception as e: print("feed error",feed,e)

if news:
    data["news"]=news[:50]
data["updated_at"]=str(date.today())

with open(path,"w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
print("Updated",path)
