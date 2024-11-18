import json
import os

class Album():
    def __init__(self, title, artist, sales, year, genre):
        self.title = title
        self.artist = artist
        self.sales = sales
        self.year = year
        self.genre = genre

title = input("What is the name of the song you want to save?")
artist = input("Who made the song?")
sales = input("How many copies did it sell?")
year = input("What year was the song released?")
genre = input("What is the genre of the song?")

x = Album(title, artist, sales, year, genre)
print(vars(x))


with open("./json/skib.json", "r") as f:
    album = json.load(f)
    album.append(vars(x))

new_file = "updated.json"

with open(new_file, "w") as f:
    json_string = json.dumps(album)
    f.write(json_string)

os.remove("./json/skib.json")
os.rename(new_file, "./json/skib.json")

#File two 
def sort():
    user_int = input("Would you like to sort by title, artist, sales, year, or genre? ").strip()
    if user_int == "title":
        title = input("What is the name of the album you want to know?")
        list = []
        for song in album:
            if title == song["title"]:
                list.append(song)
                print(list)
    if user_int == "artist":
        artist = input("What is the name of the artist of the album you want to know?").strip()
        Artist = []
        for skibidi in album:
            if artist == skibidi["artist"]:
                Artist.append(skibidi)
                print(Artist)
    if user_int == "sales":
        sales = input("What is the number of sales you want to know?")
        Sale = []
        for shaka in album:
            if sales == shaka["sales"]:
                Sale.append(shaka) 
                print(Sale)
    if user_int == "year":
        year = input("What is the release year of the album you want to know?")
        years = []
        for boom in album:
            if year == boom["year"]:
                years.append(boom)
                print(years)
    if user_int == "genre":
        genre = input("What is the genre of the album you want to know?")
        genres = []
        for ding in album:
            if genre == ding["genre"]:
                genres.append(ding)
                print(genres)
sort()


