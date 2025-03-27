import requests

API_TOKEN = "IUatdbg7HcTN2EnzCz-2mwUlp11_3Xz4YwNPqd9Lvt-oWVOj"
API_URL = "https://api.currentsapi.services/v1/latest-news"

def fetch_articles():
    try:
        headers = {
            'Authorization': API_TOKEN
        }
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('news', [])
            return [(article['title'], article['url']) for article in articles if article.get('title') and article.get('url')]
        else:
            print("❌ Erreur API :", response.status_code, "-", response.text)
            return []
    except Exception as e:
        print("❌ Erreur lors de la récupération des articles :", e)
        return []