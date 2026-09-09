# Task 2 - Scrape Images from a Website

## What the project does

This program opens the public practice website **Books to Scrape** with
Selenium. BeautifulSoup finds every image on the page, including images whose
`src` contains a relative URL. `urljoin()` changes each relative URL into an
absolute URL. The program saves all URLs in `image_urls.txt` and uses Requests
to download the first 10 images into a folder named `downloaded_images`.


## Libraries used

- `selenium`: opens the webpage and gets its HTML.
- `BeautifulSoup`: finds all `<img>` elements in the HTML.
- `requests`: downloads the image files.
- `urllib.parse`: converts relative URLs into absolute URLs.
- `os` and `re`: create the folder and make filenames.

## How to run the code

1. Install Firefox.
2. Open a terminal inside the `Task_2` folder.
3. Install the libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python Task_15_Q2.py
   ```


## Example output

```text
Opening the website...
Found 20 image URLs.
...
All image URLs were saved in image_urls.txt
Downloaded: 01_image10.jpg
Downloaded: 02_image10.jpg
...
Downloaded: 10_image10.jpg
All images were downloaded in downloaded_images folder
```
