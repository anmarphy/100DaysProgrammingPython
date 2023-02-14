from bs4 import BeautifulSoup
import requests

date_info = input("Which day do you want to track? Format: YYYY-MM-DD ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date_info}")
billboard=response.text
soup=BeautifulSoup(billboard, "html.parser")

songs= soup.find_all("h3", class_="a-no-trucate")

songs_names = []
for song in songs:
    song_name = song.getText()
    song_name=song_name.replace("\n", '')
    song_name = song_name.replace('\t', '')
    songs_names.append(song_name)
print(songs_names)



