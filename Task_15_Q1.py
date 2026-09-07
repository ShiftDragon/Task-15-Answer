import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
requests.get(url)
website = requests.get(url).text
html_website = BeautifulSoup(website , "html")

#page title
title = html_website.title.text
print(title)

#headers
headers = html_website.find_all(["h1",'h2','h3'])
for header in headers:
    print(header.text)

#links
links = html_website.find_all("a",class_="tag")
print("\n===== 5 LINKS =====")

count = 0

for link in links:
    href = link.get("href")

    if href:
        print(href)
        count += 1

    if count == 5:
        break

#all website pages
for i in range(1,11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    website = requests.get(url).text
    html_website = BeautifulSoup(website , "html")
    quotes = html_website.find_all("div", class_="quote")
    print(f"\n========== Page {i} ==========\n")
    for quote in quotes:
        quote_text = quote.find("span", class_="text").text
        quote_person = quote.find("small", class_="author").text
        print(quote_text,"By:",quote_person)
        print('--------------')

    print("\n")