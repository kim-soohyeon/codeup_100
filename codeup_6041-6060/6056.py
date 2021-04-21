# https://codeup.kr/problem.php?id=6056
# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = map(int,input().split())
a= bool(a)
b= bool(b)

# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.
# (A&&!B)||(!A&&B)

print((a and (not b)) or ((not a) and b))