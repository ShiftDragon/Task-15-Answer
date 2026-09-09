# Task 15 - Web Scraping

## What the project does
This Python project scrapes data from:

https://quotes.toscrape.com/

The program:
- Sends requests to the website.
- Extracts and displays the page title.
- Extracts and displays headings.
- Visits pages 1 to 10.
- Extracts quotes and their authors.
- Organizes the output by page.

## Libraries used
- `requests` - sends HTTP requests to the website.
- `beautifulsoup4` - reads and extracts data from the HTML page.

## How to run the code

1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required libraries:


pip install -r requirements.txt


4. Run the Python file:

python Task_15_p1.py

## Example output

```text
Quotes to Scrape

Top Ten tags

===== 5 LINKS =====
/tag/change/page/1/
/tag/deep-thoughts/page/1/
/tag/thinking/page/1/
/tag/world/page/1/
/tag/abilities/page/1/

========== Page 1 ==========

“The world as we have created it is a process of our thinking.
It cannot be changed without changing our thinking.”
By: Albert Einstein
--------------

========== Page 2 ==========

...
```


