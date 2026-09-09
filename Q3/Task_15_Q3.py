from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import re
import time

youtube_url = "https://www.youtube.com/feed/channels"
output_file = "youtube_subscriptions.csv"

# Use the existing Firefox profile.
profile_path = r"C:\Users\osabr\AppData\Roaming\Mozilla\Firefox\Profiles\euysm2zo.default-release"


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("-profile")
firefox_options.add_argument(profile_path)

print("Starting Firefox...")
driver = webdriver.Firefox(options=firefox_options)

print("Opening YouTube...")
driver.get(youtube_url)
time.sleep(5)

# Scroll to get more subscriptions
for scroll in range(10):
    driver.execute_script("window.scrollBy(0,100);")
    time.sleep(1)

website = driver.page_source
driver.quit()

# Extracting channels information and formating them before store it
html_website = BeautifulSoup(website, "html")

channel_cards = html_website.select(
    "ytd-channel-renderer, ytd-grid-channel-renderer"
)

print(f"Found {len(channel_cards)} channel cards.")


channels = []
used_urls = set()

for channel_card in channel_cards:
    link = channel_card.select_one(
        'a#main-link[href], a[href^="/@"], a[href^="/channel/"], '
        'a[href^="/c/"], a[href^="/user/"]'
    )

    

    channel_url = urljoin("https://www.youtube.com", link.get("href"))

    if channel_url in used_urls:
        continue

    name_element = channel_card.select_one(
        "yt-formatted-string#text, #channel-title, #text"
    )

    if name_element:
        channel_name = name_element.get_text(" ", strip=True)
    else:
        channel_name = (
            link.get("title")
            or link.get("aria-label")
            or "Unknown"
        )

        # Backup search if YouTube changes the subscriber element ID.
    card_text = channel_card.get_text(" ", strip=True)
    match = re.search(
        r"[\d.,]+(?:K|M|B)?\s+subscribers?",
        card_text,
        re.IGNORECASE
    )

    if match:
        subscriber_count = match.group(0)
    else:
        subscriber_count = "Not publicly available"

    channels.append({
        "Channel Name": channel_name,
        "Channel URL": channel_url,
        "Subscriber Count": subscriber_count
    })

    used_urls.add(channel_url)


columns = ["Channel Name", "Channel URL", "Subscriber Count"]
dataframe = pd.DataFrame(channels, columns=columns)
dataframe.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"\nFound {len(dataframe)} subscribed channels.")
print(dataframe.to_string(index=False))
print(f"\nThe results were saved in: {output_file}")