import urllib3
import requests
import pandas
import csv
import json
from pandas.io.json import json_normalize
""" import urllib """
from bs4 import BeautifulSoup



""" pandas.read_json(data).to_excel("test.xlsx") """

data = []



""" with open(data) as data_file:
    test = json.load(data_file)

df = json_normalize(test) """

""" def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val """
page_query = 36
amount = 1
totalAmount = 0
while (amount > 0):
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

with open(data) as fi:
    data = json.load(fi)
    df = pandas.DataFrame(data=data['rows'],columns=data['headings'])
    df.to_csv('data_table.csv', index=False)

print(totalAmount)

""" print(i) """
""" pandas.read_json(data) """
""" test = json.loads(data)
f = csv.writer(open("test.csv", "wb+")) """
"""     print(n['data-project'])
    pandas.read_json(n['data-project']).to_excel("test.xlsx") """
""" print(data) """
""" with open("output.csv", "w", newline="") as f: """

""" for i in data:
    print(format(i))
data = soup.div["data-project"] """

""" print(data) """


""" print(soup.prettify()) """

