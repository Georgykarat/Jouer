import csv
import requests
from bs4 import BeautifulSoup


# Set your login credentials
username = 'gitekaw712@asuflex.com'
password = '85?v_jvB$4JRrVe'

import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Create an empty DataFrame to store the board game data
boardgames_df = pd.DataFrame(columns=['Game ID', 'Name', 'Description', 'Year Published', 'Min Players', 'Max Players', 'Playing Time'])

for i in range(1, 200944):
    try:
        # Send a GET request to the API endpoint for the current board game ID
        url = f'https://boardgamegeek.com/xmlapi/boardgame/{i}'
        response = requests.get(url)

        # Parse the XML data for the current board game
        root = ET.fromstring(response.content)

        # Extract the relevant information for the current board game
        game_id = str(i)
        name = root.find('boardgame/name').text.strip() if root.find('boardgame/name') is not None else ''
        print(f"{i}. {name}")
        description = root.find('boardgame/description').text.strip() if root.find('boardgame/description') is not None else ''
        year_published = root.find('boardgame/yearpublished').text.strip() if root.find('boardgame/yearpublished') is not None else ''
        min_players = root.find('boardgame/minplayers').text.strip() if root.find('boardgame/minplayers') is not None else ''
        max_players = root.find('boardgame/maxplayers').text.strip() if root.find('boardgame/maxplayers') is not None else ''
        playing_time = root.find('boardgame/playingtime').text.strip() if root.find('boardgame/playingtime') is not None else ''

        # Add the board game data to the DataFrame
        boardgames_df = boardgames_df.append({'Game ID': game_id, 'Name': name, 'Description': description,
                                              'Year Published': year_published, 'Min Players': min_players,
                                              'Max Players': max_players, 'Playing Time': playing_time}, ignore_index=True)

        print(f'Processed board game with ID: {game_id}')

    except ET.ParseError as e:
        print(f'Error parsing XML data for board game with ID: {i}, {e}')

# Save the DataFrame to a CSV file
boardgames_df.to_csv('boardgames.csv', index=False)

print('Board games data has been successfully parsed and saved to "boardgames.csv".')