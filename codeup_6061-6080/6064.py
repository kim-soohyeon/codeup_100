# https://codeup.kr/problem.php?id=6064
# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기

# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.
a,b,c=map(int,input().split())

# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값

num= a if a<=b else b
print(num if num<=c else c)