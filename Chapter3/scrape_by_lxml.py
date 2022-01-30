import lxml.html

#html 파일을 일고 들이고, getroot() 메소드로 HtmlElement 객체를 생성
tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()

#cssselect() 메소드로 a 요소의 리스트를 추출하고 반복을 돌립니다.
for a in html.cssselect('a'):
    #href 속성과 글자를 추출합니다.
    print(a.get('href'), a.text)