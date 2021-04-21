# https://codeup.kr/problem.php?id=6042
# 6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기

# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

f1,f2= map(float,input().split())

#  나눗셈(division)을 계산하는 연산자(/)
print(format(f1/f2, ".3f"))


