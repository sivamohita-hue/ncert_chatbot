import requests
from bs4 import BeautifulSoup


def fetch_answer(query):

    url = f"https://www.google.com/search?q={query}"

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    snippets = soup.select(".BNeawe")

    if snippets:
        return snippets[0].text

    return "No answer found"
