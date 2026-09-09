# Task 15 Q3 - Get YouTube Subscription Information

## What the project does

This program opens the signed-in user's YouTube channels page. Selenium scrolls
down to load the subscriptions. BeautifulSoup reads the loaded HTML and
extracts the channel name, channel URL, and subscriber count. Pandas stores the data in a DataFrame and exports it to
`youtube_subscriptions.csv`.

The program accesses only the account that the user personally signs in to.

## Libraries used

- `selenium`: opens YouTube and scrolls through the channels.
- `BeautifulSoup`: extracts information from the loaded HTML.
- `pandas`: creates the DataFrame and CSV file.
- `urllib.parse`: converts channel links into complete URLs.
- `os`, `re`, and `time`: support the browser profile, text matching, and waits.

## How to run the code

1. Install Firefox.
2. Open a terminal inside the `Q3` folder.
3. Install the libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python Task_15_Q3.py
   ```

5. A separate Firefox window will open. 
6. Wait until the subscribed-channels page appears.
7. Wait for the script to finish and open `youtube_subscriptions.csv`.



## Example output

```text
Starting Firefox...

Opening YouTube...
Found 5 channel cards.
Found 5 subscribed channels.

   Channel Name                         Channel URL Subscriber Count
PewDiePie PewDiePie https://www.youtube.com/@PewDiePie              109M subscribers

The results were saved in: youtube_subscriptions.csv
```
