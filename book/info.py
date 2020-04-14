def extract_info(book_list):
    result = []
    i=0
    
    while i <len(book_list):
        # print('len:', len(book_list))
        book = book_list[i]

        img_src = book.find('img')['src']

        info = book.find("td",{"class":"goodsTxtInfo"})

        p_list = book.find_all('p')
        title = p_list[0].text.strip()

        a_list = info.find('div', {'class' : 'aupu'}).find_all('a')

        author = a_list[0].string

        publisher = a_list[1].string

        price = p_list[1].find('span', {'class', 'priceB'}).string
        
        summary_total = book_list[i+1].find('p', {'class' : 'read'})

        if(summary_total):
            summary = summary_total.string.strip()
        else:
            summary = ''

        print('i :', i)
        
        book_info = {
            'title' : title,
            'price' : price,
            'img_src' : img_src,
            'author' : author,
            'publisher' : publisher,
            'summary' : summary,
        }

        i += 2

        result.append(book_info)
    # print(result)
    return result