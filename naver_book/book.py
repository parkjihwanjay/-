import requests
from bs4 import BeautifulSoup
from info import extract_info
import csv

file = open("naver_book.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "price", "img_src", 'link', 'author', 'publisher', 'intro'])

final_result = []

# 예외처리 없으면 5까지
# 예외처리하면 8까지
for i in range(10):
    # print('몇번째 : ', i)
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol", {"class" : "basic"})
    book_list = book_list_box.find_all('li')

    final_result = final_result + extract_info(book_list)

for result in final_result:

    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['img_src'])
    row.append(result['link'])
    row.append(result['author'])
    row.append(result['publisher'])
    row.append(result['intro'])

    writer.writerow(row)

print(final_result)