# https://codeup.kr/problem.php?id=6094
# 6094 : [기초-리스트] 이상한 출석 번호 부르기3

# 입력
# 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
# n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
#
# 출력
# 출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

n=int(input())
k=input().split()

for i in range(n):
  k[i]=int(k[i])

small=k[0]
for i in range(n):
  if small>=k[i]:
    small=k[i]

print(small)
