import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.ndtv.com/latest"   # Public news website

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch the webpage. Status Code:", response.status_code)
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # NDTV headlines are inside <h2> tags
        headlines = soup.find_all("h2")

        cleaned_headlines = []

        for h in headlines:
            text = h.get_text(strip=True)
            if text:
                cleaned_headlines.append(text)

        # Save to file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for line in cleaned_headlines:
                file.write(line + "\n")

        print("Headlines saved to headlines.txt")

    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    scrape_headlines()
