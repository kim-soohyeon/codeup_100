# https://codeup.kr/problem.php?id=6047
# 6047 : [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기

# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

a,b = map(int,input().split())

print(a<<b)

