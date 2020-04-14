import requests
from bs4 import BeautifulSoup
from info import extract_info
import csv

file = open("books.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "price", "img_src", 'author', 'publisher', 'summary'])

final_result = []

# 예외처리 없으면 5까지
# 예외처리하면 8까지
for i in range(8):
    # print('몇번째 : ', i)
    book_html = requests.get(f'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber={i+1}')
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("table", {"id" : "category_layout"})
    book_list = book_list_box.find_all('tr')

    final_result = final_result + extract_info(book_list)

for result in final_result:

    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['img_src'])
    row.append(result['author'])
    row.append(result['publisher'])
    row.append(result['summary'])

    writer.writerow(row)

print(final_result)