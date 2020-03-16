import json
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.rbnz.govt.nz/monetary-policy/official-cash-rate-decisions'
html = requests.get(url).text
soup = bs(html, "html.parser")

data_table = soup.find('table', class_='table')
data = []

for row in data_table.findAll('tr')[1:]:
    item = row.findAll('td')
    link = item[0].find('a', href=True)
    url = f"https://www.rbnz.govt.nz{link['href']}" if link else ""
    data.append({
        'date': " ".join(item[0].text.split()),
        'change': item[1].text.strip(),
        'rate': item[2].text.strip(),
        'link': url,
    })

print(json.dumps(data))
