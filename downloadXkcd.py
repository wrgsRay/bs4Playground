from bs4 import BeautifulSoup as bs
import requests, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs(res.text)
    # Find the URL of the comic image.

    # Download the image

    # Save the image to ./xkcd

    # Get the Prev button's url.

print('Done.')
