# https://codeup.kr/problem.php?id=6019
# 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기

# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

y,m,d=input().split('.')

print(d,m,y,sep='-')