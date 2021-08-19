import requests
from bs4 import BeautifulSoup
import csv

url = "https://htmlcolorcodes.com/colors/shades-of-blue/"

page = requests.get(url)  # Gets the url, checks the response - if 4xx/5xx, error. 200 means all a-OK.

soup = BeautifulSoup(page.content, "html.parser")  # Work out what this means.

page_table_name = soup.find_all(class_="color-table__cell color-table__cell--name")  # Finds all tabled class (name).

page_table_hex = soup.find_all(class_="color-table__cell color-table__cell--hex")  # Finds all tabled class (hex)

name_lst = []  # New lists... need I explain more?
hexa_lst = []  # Seriously?

for name in page_table_name:  # For each individual table within table, print out the text.
    string = name.get_text()  # Assigns the fetched name into a string.
    string = string.replace('\n', "")  # Replaces those '\n' into '' (empty space).
    name_lst.append(string)  # Appends the string into a list.

for hexa in page_table_hex:  # For each individual table within table, print out the text.
    hexa_lst.append(hexa.get_text())  # Gets the hexadecimal text and appends into a list.

datafile = open("data.csv", "w")
writer = csv.writer(datafile)
for f in range(len(name_lst)):
    writer.writerow([name_lst[f], hexa_lst[f]])
datafile.close()
