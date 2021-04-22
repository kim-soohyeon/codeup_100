# https://codeup.kr/problem.php?id=6097
# 6097 : [기초-리스트] 설탕과자 뽑기

# 입력
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w
#
# 출력
# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
# 단, 각 숫자는 공백으로 구분하여 출력한다.

h,w = map(int,input().split())# 격자판의 세로(h), 가로(w)
n=int(input()) # 막대의 개수(n)
matrix=[[0 for _ in range(w)]for _ in range(h)]

for _ in range(n):
  l,d,x,y = map(int,input().split())# 막대의 길이(l), 방향(d), 좌표(x, y)
  x-=1
  y-=1
  for _ in range(l):
    matrix[x][y] = 1
    if d==0:
      y += 1
    else:
      x += 1

for i in range(h):
  print(*matrix[i])