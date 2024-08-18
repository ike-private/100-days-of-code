import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

import requests

response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
movies = []

for movie_title in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn"):
    movie = movie_title.text
    movies.append(str(movie))




with open('new_movies.txt', 'w') as f:
    for line in reversed(movies):
        f.write(f"{line}\n")


