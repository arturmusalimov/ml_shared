import requests
from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/"

response = requests.get(url = url)
response.raise_for_status()

website = response.content
soup = BeautifulSoup(website, "html.parser")
results = soup.select("tr")

for tr in results:
    print(tr.text)
