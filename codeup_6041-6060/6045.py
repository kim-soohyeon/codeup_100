# https://codeup.kr/problem.php?id=6045
# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기

# 정수 3개를 입력받아 합과 평균을 출력해보자.
# 합과 평균을 공백을 두고 출력한다.
# 평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

a,b,c= map(int,input().split())

print(a+b+c,'%.2f'%((a+b+c)/3))

