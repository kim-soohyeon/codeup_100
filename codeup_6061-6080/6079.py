# https://codeup.kr/problem.php?id=6079
# 6079 : [기초-종합] 언제까지 더해야 할까?

# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.



a=int(input())
i=0
sum=0

# 1+2+3+4+5+6+7+8+9+10 = 55
while sum<a:
   i += 1
   sum+=i

print(i)