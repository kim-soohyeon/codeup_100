# https://codeup.kr/problem.php?id=6022
# 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기

# 6자리의 연월일(YYMMDD)을 입력받아 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

a = input()

# 마지막 값-1까지 slicing
# ex) 0:2이면 0부터 1까지
print(a[0:2],a[2:4],a[4:6])