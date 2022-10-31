# scraping the list of 100 greatest movies of all times
from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

res = requests.get(URL)
empireonline_website = res.text

EO_soup = BeautifulSoup(empireonline_website, 'html.parser')

movies_list = []

elements = EO_soup.find_all(name='picture')
for elem in elements:
    elem_img = elem.find_all(name='img')
    movies_list.append(elem_img[0]['alt'])

print(movies_list)

with open('movies_list.txt', mode='w+') as file:
    for movie in movies_list[::-1]:
        file.write(f'{movie}\n')
