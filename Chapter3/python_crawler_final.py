import re
import requests
import lxml.html
import MySQLdb


def main():
    #여러 페이지에서 크롤링할 것으로 Session을 사용합니다.
    conn = MySQLdb.connect(db='scraping', user='root', passwd='1325', charset='utf8mb4')
    c = conn.cursor()
    c.execute('drop table if exists books')
    c.execute("""
        create table books(
            url varchar(200),
            title varchar(100),
            price varchar(6),
            conent varchar(50));
    """)

    session = requests.Session()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url) #Session을 사용해 상세 페이지를 추출합니다.
        ebook = scrape_detail_page(response) #상세 페이지에서 상세 정보를 추출합니다.

        c.execute('insert into books values (%(url)s, %(title)s, %(price)s, %(content)s);', ebook)
        print(ebook) #책 관련 정보를 출력합니다.

    conn.commit()
    conn.close()


def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url


def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content())
                    for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
                    if normalize_spaces(p.text_content()) != '']
    }

    if len(ebook.get('content')):
        return {'url': ebook.get('url'), 'title': ebook.get('title'), 'price': ebook.get('price'), 'content': ebook.get('content')[0]}
    else:
        return {'url': ebook.get('url'), 'title': ebook.get('title'), 'price': ebook.get('price'), 'content': ''}


def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경합니다.
    """
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    main()