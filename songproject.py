from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

print("""
--------------- WELCOME TO SONG SUGGESTER BOT ---------------

1- ROCK
2- METAL
3- SOUNDTRACKS

Pick a genre and then I randomly choose a song!
(If you want to quit program, press 'q'.)

""")

while True:
    genre = input("Which genre do you want?: ")
    
    if(genre == "1"):
        playlist = "https://www.youtube.com/playlist?list=PLtvZD3X4IjsP_pViWs9F9feAjDkeBl0Bq"
    elif(genre == "2"):
        playlist = "https://www.youtube.com/playlist?list=PLtvZD3X4IjsMuNxFe2svU_O5N8Gm36wKl"
    elif(genre == "3"):
        playlist = "https://www.youtube.com/playlist?list=PLtvZD3X4IjsPB2kQdo1lWydSHyAg_ecX_"
    else:
        print("Shutting Down...")
        time.sleep(3)
        break

    # start web browser
    browser=webdriver.Firefox()

    songs = []
    link = []

    # get source code
    browser.get(playlist)
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    videospan = soup.find_all("span", id="video-title")

    for span in videospan:
        songs.append(span.text)

    

    print("Enjoy your song!: ", random.choice(songs))
    songs.clear()

    # close web browser
    browser.close()