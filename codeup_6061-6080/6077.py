# https://codeup.kr/problem.php?id=6077
# 6077 : [기초-종합] 짝수 합 구하기

# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

a=int(input())

sum=0
for i in range(a+1):
   if i%2==0:
      sum+=i
print(sum)