from bs4 import BeautifulSoup

with open('./website.html', mode='r') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.string)

# print(soup.find_all(name='a')[:])

anchor_tags = soup.find_all(name='a')

for tag in anchor_tags:
    print(tag['href'])
    print(tag.getText())

heading = soup.find_all(name='h1')
title_heading = heading['id' == 'name']
print(title_heading.string)

