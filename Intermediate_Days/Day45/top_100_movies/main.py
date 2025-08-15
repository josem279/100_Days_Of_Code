import requests
from bs4 import BeautifulSoup
import os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_text = response.text

soup = BeautifulSoup(movies_text, "html.parser")

all_movies = soup.find_all("h3")
movie_titles = [movie.getText() for movie in all_movies]
movie_titles = movie_titles[::-1]

with open(r'Intermediate_Days\Day45\top_100_movies\movie_titles.txt', "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")