def extract_info(book_list):
    result = []
    i=0
    
    for book in book_list:
        img_src = book.find('img')['src']
        title = book.find('a', {'class' : 'N=a:bta.title'}).string
        link = book.find('a', {'class' : 'N=a:bta.author'})['href']
        author = book.find('a', {'class' : 'N=a:bta.author'}).string
        publisher = book.find('a', {'class' : 'N=a:bta.publisher'}).string

        price_box = book.find('em', {'class' : 'price'})

        if price_box:
            price = price_box.string
        else:
            price = '없음'

        dd_list = book.find('dl').find_all('dd')
        contents = dd_list[-1].contents
        intro = contents[1].strip()

        book_info = {
            'title' : title,
            'price' : price,
            'img_src' : img_src,
            'link' : link,
            'author' : author,
            'publisher' : publisher,
            'intro' : intro,
        }

        result.append(book_info)

    # print(result)
    return result