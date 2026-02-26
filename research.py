import feedparser

def fetch_papers():
    url = "http://export.arxiv.org/rss/cs.AI"
    feed = feedparser.parse(url)

    papers = []

    for entry in feed.entries[:3]:
        papers.append({
            "title": entry.title,
            "summary": entry.summary
        })

    return papers