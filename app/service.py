import requests
from app.utils import save_document
from app import CORE_API_KEY, CORE_API_URL


def fetch_core_articles(query, limit=10):
    params = {"q": query, "limit": limit}
    headers = {"Authorization": f"Bearer {CORE_API_KEY}"}
    resp = requests.get(CORE_API_URL, params=params, headers=headers)

    if resp.status_code != 200:
        print(f"[CORE] Erro: {resp.status_code} - {resp.text}")
        return

    data = resp.json()
    for item in data.get("results", []):
        title = item.get("title", "Sem título")
        url = item.get("links", [{}])[0].get("url", "")
        abstract = item.get("abstract", "")
        if abstract:
            save_document(title, url, abstract, source="CORE")

def fetch_wikiquote_quotes(topic, limit=5):
    api_url = "https://en.wikiquote.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": topic,
        "prop": "extracts",
        "explaintext": True
    }
    resp = requests.get(api_url, params=params)
    data = resp.json()

    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        text = page.get("extract", "")
        if text:
            save_document(topic, f"https://en.wikiquote.org/wiki/{topic}", text, source="WIKIQUOTE")