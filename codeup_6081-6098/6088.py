# https://codeup.kr/problem.php?id=6088
# 6088 : [기초-종합] 수 나열하기1

# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
# n번째 수를 출력하는 프로그램을 만들어보자.

# 입력
# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)
#
# 출력
# n번째 수를 출력한다.

a,d,n=map(int,input().split())
sum=a

for i in range(1,n):
    sum+=d

print(sum)





