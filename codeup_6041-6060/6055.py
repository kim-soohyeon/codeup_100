# https://codeup.kr/problem.php?id=6055
# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기

# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = map(int,input().split())

if bool(a) or bool(b):
    print('True')
else:
    print('False')