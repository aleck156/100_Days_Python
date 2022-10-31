# find the top 100 music that was all the hot stuff back in the author's teenage years
# get users birthyear
# add 15
# URL = f'https://billboard.com/charts/hot-100/{year}-{month}-{day}'
# fetch 100 songs off Billboard rankings from that year
# make a playlist in a spotify service

import requests
from bs4 import BeautifulSoup

# year = input('Enter your birth year:')
# month = input('Enter your birth month:')
# day = input('Enter your birth day:')
#
# if len(month) < 2:
#     month = f'0{month}'

# URL = f'https://billboard.com/charts/hot-100/{year}-{month}-{day}/'

URL = 'https://billboard.com/charts/hot-100/1986-02-16/'
res = requests.get(URL)
res_html = res.text
billboard_soup = BeautifulSoup(res_html, 'html.parser')

# print(billboard_soup)
entry_rows = billboard_soup.find_all(class_='o-chart-results-list-row-container')
for entry_row in entry_rows:
    # all_spans = entry_row.find_all(name='span', class_='c-label')
    # entry_row_number = all_spans[0].getText().strip()
    # entry_row_artist = all_spans[1].getText().strip()
    all_li_elements = entry_row.find_all(name='li')
    entry_row_number = all_li_elements[0].find(name='span', class_='c-label').getText().strip()
    entry_row_title = entry_row.find(name='h3', id='title-of-a-story').getText().strip()
    # entry_row_artist = entry_row.find(name='li', class_='o-chart-results-list__item').find(name='span', class_='c-label').getText().strip()
    print(entry_row_number, entry_row_title)
    # print(f'{entry_row_number})\t{entry_row_artist}\t{entry_row_title}')
