# https://codeup.kr/problem.php?id=6033
# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기

# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

a = ord(input())

print(a)
print(chr(a+1))
