# https://codeup.kr/problem.php?id=6091
# 6091 : [기초-종합] 함께 문제 푸는 날

# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
# 예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

# 입력
# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
# 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)
#
# 출력
# 3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

a,b,c=map(int,input().split()) # 방문 주기
d=1 # 날 수

# 최소공배수 구하기
while d%a!=0 or d%b!=0 or d%c!=0:
    d+=1
print(d)



