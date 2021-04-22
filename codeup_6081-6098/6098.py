# https://codeup.kr/problem.php?id=6098
# 6098 : [기초-리스트] 성실한 개미

# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.
#
# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.
#
# 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

# 입력
# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
#
# 출력
# 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

matrix=[]
for _ in range(10):
  matrix.append(input().split())

for i in range(10):
  for j in range(10):
    matrix[i][j]=int(matrix[i][j])

x,y=1,1
m=0

while m!=2 and x<10 and y<10:
  m=matrix[x][y]
  if m!=1:
    matrix[x][y]=9
    y+=1
  else:
      x += 1
      y-=1

for i in range(10):
  print(*matrix[i])