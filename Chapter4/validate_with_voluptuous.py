from voluptuous import Schema, Match

#다음 4개의 규칙을 가진 스키마를 정의합니다.
schema = Schema({ #규칙1: 객체는 dict
    'name': str,  #규칙2: name은 str
    'price': Match(r'^[0-9,]+$'), #규칙3: price가 정규 표현식에 맞는지 확인
}, required=True) #규칙4: dict의 키는 필수

#Schema 객체는 함수처럼 호출해서 사용합니다.
#매개변수에 대상을 넣으면 유효성 검사를 수행합니다.
schema({
    'name': '포도',
    'price': '3,000',
})

# schema({
#     'name': None,
#     'price': '3,000',
# })