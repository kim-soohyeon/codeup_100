# https://codeup.kr/problem.php?id=6071
# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기

# 임의의 정수가 줄을 바꿔 계속 입력된다.
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

a=1
while a!=0:
    a=int(input())
    if a!=0:
        print(a)
    else:
        break