# 주민등록번호
# 901201-1111111

# 이메일 주소
# yajang12@gmail.com
# yajang12@gmail@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.0.1
# 1000.2000.3000.4000

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | sea (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 매치되지 않으면 에러가 발생
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("case")
# m = p.match("cafe")
# m = p.match("caffe")
# m = p.match("good care")
# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)


# 총정리
# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 3. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se&)  : 문자열의 끝 > case, base (O) | sea (X)

# 정규식 표현 참조
# w3 → python → regular expression
# python re