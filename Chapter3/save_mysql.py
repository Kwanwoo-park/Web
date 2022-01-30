import MySQLdb

#MySQL 서버에 접속하고 연결에 변수에 저장합니다.
#사용자 이름과 비밀번호를 지정한 뒤 scraping 데이터베이스를 사용합니다.
#접속에 사용할 문자 코드는 utf8mb4로 지정합니다.
conn = MySQLdb.connect(db='scraping', user='root', passwd='1325', charset='utf8mb4')

c = conn.cursor()

c.execute('drop table if exists cities;')

c.execute("""
    create table cities (
        id int,
        city varchar(20),
        population int
    );
""")

c.execute('insert into cities values(%s, %s, %s);', (1, '상하이', 24150000))

c.execute('insert into cities values (%(id)s, %(city)s, %(population)s);',
          {'id': 2, 'city': '카라치', 'population': 23500000})

c.executemany('insert into cities values(%(id)s, %(city)s, %(population)s);', [
    {'id': '3', 'city': '베이징', 'population': '21516000'},
    {'id': '4', 'city': '텐진', 'population': '14722100'},
    {'id': '5', 'city': '이스탄불', 'population': '14160467'},
])

conn.commit()

c.execute('select * from cities;')

for row in c.fetchall():
    print(row)

conn.close()