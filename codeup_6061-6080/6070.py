# https://codeup.kr/problem.php?id=6070
# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기

# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

a=int(input())

if a==12 or a==1 or a==2:
    print("winter")
elif a>=3 and a<=5:
    print("spring")
elif a>=6 and a<=8:
    print("summer")
elif a >= 9 and a <= 11:
    print("fall")