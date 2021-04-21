# https://codeup.kr/problem.php?id=6027
# 6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1

# 10진수를 입력받아 16진수(hexadecimal)소문자 형태 문자열로  출력해보자.
# 10진수: 0 1 2 3 4 5 6 7 8 9
# 16진수: 0 1 2 3 4 5 6 7 8 9 a b c d e f

a = int(input())

# 16진수(hexadecimal)
print('%x'% a)