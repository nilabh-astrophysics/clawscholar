import feedparser

try:
    import ollama
    OLLAMA_AVAILABLE = True
except:
    OLLAMA_AVAILABLE = False


def fetch_papers(query):
    url = f"https://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=1"
    feed = feedparser.parse(url)

    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "summary": entry.summary
        })

    return papers


def summarize_paper(paper, mode):
    text = paper["summary"]

    if OLLAMA_AVAILABLE:
        try:
            response = ollama.chat(
                model="llama3",
                messages=[
                    {"role": "user", "content": f"Summarize this in {mode} detail:\n\n{text}"}
                ]
            )
            return response["message"]["content"]
        except:
            pass

    # Fallback if Ollama not available (Cloud safe)
    if mode == "advanced":
        return f"Advanced Analysis:\n\n{text[:1000]}"
    else:
        return f"Basic Summary:\n\n{text[:500]}"
