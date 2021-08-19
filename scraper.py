#import main  # Imports main.py file

import requests
from bs4 import BeautifulSoup

url = "https://htmlcolorcodes.com/colors/shades-of-blue/"

page = requests.get(url)  # Gets the url, checks the response - if 4xx/5xx, error. 200 means it's all good.

soup = BeautifulSoup(page.content, "html.parser")  # Work out what this means.

page_finder = soup.find_all('td')  # Fetches the 'td' (table) part of HTML.

print(page_finder)  # Prints the outcome.