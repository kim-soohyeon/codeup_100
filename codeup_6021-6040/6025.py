# https://codeup.kr/problem.php?id=6025
# 6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기

# 정수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

a,b = input().split()

# 입력받은 값이 문자열이기 때문에 각각 int()처리하여 정수형으로 변환
print(int(a)+int(b))