from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse
import time
import os
import re

browser = webdriver.Firefox()
website_url = "https://books.toscrape.com/"
browser.get(website_url)
time.sleep(2)
website = browser.page_source
browser.quit()
html_website = BeautifulSoup(website, "html")
image_tags = html_website.find_all("img")

images = []

for image_tag in image_tags:
    image_source = image_tag.get("src")

    if image_source:
        image_url = urljoin(website_url, image_source)
        image_name = image_tag.get("alt", "image")
        images.append({"name": image_name, "url": image_url})

print(f"Found {len(images)} image URLs.")

for image in images:
    print(image["url"])

with open("image_urls.txt", "w", encoding="utf-8") as file:
    for image in images:
        file.write(image["url"] + "\n")

print("All image URLs were saved in image_urls.txt")


os.makedirs("downloaded_images", exist_ok=True)

downloaded_count = 0

for image in images:
    if downloaded_count == 10:
        break

    try:
        # Sendig the request checking that the request worked correctly
        response = requests.get(
            image["url"],
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )
        response.raise_for_status()

        downloaded_count += 1

        for i in range (1,11):
            name = f"image{i}"

        extension = os.path.splitext(urlparse(image["url"]).path)[1].lower()
        extension = ".jpg"

        file_name = f"{downloaded_count:02d}_{name}{extension}"
        file_path = os.path.join("downloaded_images", file_name)

        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {file_name}")

    except requests.RequestException as error:
        print(f"Could not download: {image['url']}")
        print(error)
print("All images were downloaded in downloaded_images folder")