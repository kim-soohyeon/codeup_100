# https://codeup.kr/problem.php?id=6087
# 6087 : [기초-종합] 3의 배수는 통과

# 입력
# 정수 1개를 입력받는다.
# (1 ~ 100)
#
# 출력
# 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되
# 3의 배수는 출력하지 않는다.

a=int(input())

for i in range(1,a+1):
    if i%3!=0:
        print(i,end=" ")





