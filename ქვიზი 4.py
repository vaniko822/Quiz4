import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

ind = 1

file = open('notebooks.csv', 'w', encoding='UTF-8-sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Price', 'Status'])

while ind<=10:
    url = 'https://imart.ge/საოჯახო-ტექნიკა/კომპიუტერული-ტექნიკა/ლეპტოპები/?page=' + str(ind)
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')

    all_components = soup.find('div', id='categories_view_pagination_contents')

    all_notebooks = all_components.find_all('div', class_='ty-column5')

    for each in all_notebooks:
        title = each.find('a', class_='product-title').text
        price = each.find('span', class_='ty-price-num').text
        status = each.find('div', class_='ty-control-group product-list-field').span.text
        file_obj.writerow([title, price, status])

    ind += 1
    sleep(randint(15,20))