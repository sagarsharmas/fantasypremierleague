import urllib, json, pandas as pd, sqlite3
from pprint import pprint

'''
# Connect Database
conn = sqlite3.connect('/home/dell/fantasy.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS PLAYERS_DATA")
cursor.execute("DROP TABLE IF EXISTS STANDINGS")
cursor.execute("DROP TABLE IF EXISTS EVENT_DATA_PICKS")

# Individual Players Data
players_data_url = "https://fantasy.premierleague.com/drf/bootstrap-static"
response = urllib.urlopen(players_data_url)
players_data = json.loads(response.read())
players_data_elements_frame = pd.DataFrame(players_data["elements"])
players_data_elements_frame.to_sql("PLAYERS_DATA",con=conn,if_exists="replace")

# League Standings Data
url = "https://fantasy.premierleague.com/drf/leagues-classic-standings/10223"
response = urllib.urlopen(url)
data = json.loads(response.read())
standings = pd.DataFrame(data["standings"]["results"])
standings.to_sql("STANDINGS",con=conn,if_exists="replace")

# Each managers from the Mini League
for user_entry in standings["entry"]:
    entry_url = "https://fantasy.premierleague.com/drf/entry/"+str(user_entry)+"/event/4/picks"
    response = urllib.urlopen(entry_url)
    event_data = json.loads(response.read())
    event_data_picks = pd.DataFrame(event_data["picks"])
    event_data_picks['User'] = user_entry
    event_data_picks.to_sql("EVENT_DATA_PICKS", con=conn, if_exists="append")


'''

def if_manager_has_player(player):
    query = """SELECT B.PLAYER_NAME,TOTAL,C.WEB_NAME FROM EVENT_DATA_PICKS A INNER JOIN STANDINGS B
    ON A.USER = B.ENTRY
    INNER JOIN PLAYERS_DATA C
    ON
    A.ELEMENT = C.ID
    WHERE
    UPPER(C.WEB_NAME) LIKE '%""" + str(player).upper() + "%' ORDER BY B.LAST_RANK"

    conn = sqlite3.connect('/home/dell/fantasy.db')
    return pd.read_sql(query, conn)

def manager_has_players(manager):
    query = """SELECT C.WEB_NAME, B.PLAYER_NAME FROM EVENT_DATA_PICKS A INNER JOIN STANDINGS B
    ON A.USER = B.ENTRY
    INNER JOIN PLAYERS_DATA C
    ON
    A.ELEMENT = C.ID
    WHERE
    UPPER(B.PLAYER_NAME) LIKE '%""" + str(manager).upper() + "%'"

    conn = sqlite3.connect('/home/dell/fantasy.db')
    return pd.read_sql(query, conn)

pprint (if_manager_has_player("shaw"))

# pprint (manager_has_players("sagar"))