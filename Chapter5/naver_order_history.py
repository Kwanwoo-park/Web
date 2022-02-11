import time
import sys
from robobrowser import RoboBrowser
from selenium import webdriver

NAVER_ID = 'akakslslzz'
NAVER_PASSWORD = 'zzqqwoo1310'

browser = RoboBrowser(
    parser='html.parser',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
)


def main():
    print('Accessing to sign in page...', file=sys.stderr)
    browser.open('https://nid.naver.com/nidlogin.login')

    assert '네이버 : 로그인' in browser.parsed.title.string

    form = browser.get_form(attrs={'name': 'frmNIDLogin'})

    form['id'] = NAVER_ID
    form['pw'] = NAVER_PASSWORD

    print('Signing in...', file=sys.stderr)
    browser.submit_form(form, headers={
        'Referer': browser.url,
        'Accept-Language': 'ko,en-US;q=0.7,en;q=0.3',
    })

    browser.open('https://order.pay.naver.com/home?tabMenu=SHOPPING&frm=s_order')
    print(browser.parsed.prettify())

    assert '네이버페이' in browser.parsed.title.string

    print_order_history()


def print_order_history():
    for item in browser.select('.p_info'):
        order = {}

        name_element = item.select_one('span')
        date_element = item.select_one('.date')
        price_element = item.select_one('em')

        if name_element and date_element and price_element:
            name = name_element.get_text().strip()
            date = date_element.get_text().strip()
            price = price_element.get_text().strip()
            order[name] = {
                'date': date,
                'price': price
            }

            print(order[name]['date'], '-', order[name]['price'] + '원')


if __name__ == '__main__':
    main()