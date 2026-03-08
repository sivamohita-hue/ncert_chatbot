import requests
from bs4 import BeautifulSoup

def fetch_answer(query):

    try:
        url = f"https://www.google.com/search?q={query}&hl=en"

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        # Try multiple selectors
        snippets = soup.select(".BNeawe")
        if snippets:
            return snippets[0].text

        snippets = soup.select("span")
        if snippets:
            return snippets[0].text

        return "No answer found"

    except Exception as e:
        return f"Error: {str(e)}"
