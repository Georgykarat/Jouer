import csv
import requests
from bs4 import BeautifulSoup

# Set your login credentials
username = 'gitekaw712@asuflex.com'
password = '85?v_jvB$4JRrVe'

# Send a POST request to the login page to retrieve a session cookie
login_url = 'https://boardgamegeek.com/login'
session = requests.session()
session.get(login_url)
login_data = {'username': username, 'password': password}
session.post(login_url, data=login_data)

# Send a GET request to the boardgame listing while including the session cookie in the headers
url = 'https://boardgamegeek.com/browse/boardgame'
response = session.get(url, headers={'referer': login_url})
soup = BeautifulSoup(response.content, 'html.parser')

# Find the total number of pages in the boardgame listing
last_page_link = soup.find('a', {'title': 'last page'})
total_pages = int(last_page_link['href'].split('/')[-1])

# Loop through each page and extract the boardgame data
boardgames_data = []
for page in range(1, total_pages + 1):
    page_url = f'https://boardgamegeek.com/browse/boardgame/page/{page}'
    page_response = session.get(page_url, headers={'referer': url})
    page_soup = BeautifulSoup(page_response.content, 'html.parser')

    # Find all tables in the page
    tables = page_soup.find_all('table')

    # Find the table containing the boardgame data
    table = None
    for t in tables:
        if 'collection_table' in t.attrs.get('class', []):
            table = t
            break

    if not table:
        print(f'Could not find table on page {page}')
        continue

    # Extract the data from the table rows and store in a list of lists
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns:
            # Extract the data from each column in the row and store in a list
            data = [column.get_text().strip() for column in columns]
            boardgames_data.append(data)

# Write the boardgames data to a CSV file
with open('boardgames.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(boardgames_data)