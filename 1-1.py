import requests
url = "https://books.toscrape.com/"

res = requests.get(url)
print(res.text)