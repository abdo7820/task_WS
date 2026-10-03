import requests
from bs4 import BeautifulSoup

url = "https://www.yallakora.com/mainpage"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    title = link.get_text(strip=True)
    href = link.get("href")

    if title and href:
        print("Title:", title)
        print("URL:", href)
        print("-" * 50)