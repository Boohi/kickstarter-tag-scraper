import requests
import json

from bs4 import BeautifulSoup


data = []

page_query = 1
amount = 1
totalAmount = 0
while (amount > 0):
    print("Scraping page " + str(page_query))
    amount = 0
    quote_page = 'https://www.kickstarter.com/discover/advanced?woe_id=0&tag_id=121&sort=magic&ref=discovery_overlay&seed=2623960&page=' + str(page_query)
    page_query = page_query + 1
    page = requests.get(quote_page).text
    soup = BeautifulSoup(page, 'html.parser')
    raw_data = soup.findAll('div', {'data-project': True})
    for n in raw_data:
        amount = amount + 1
        data.append(n['data-project'])
    totalAmount = totalAmount + amount
print(totalAmount)
with open('dataset.json', "w") as json_file:
    json.dump(data, json_file)


