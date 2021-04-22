# https://codeup.kr/problem.php?id=6096
# 6096 : [기초-리스트] 바둑알 십자 뒤집기

# 입력
# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.
#
# 출력
# 십자 뒤집기 결과를 출력한다.

matrix=[]

for _ in range(19):
  matrix.append(input().split())

for i in range(19):
  for j in range(19):
    matrix[i][j]=int(matrix[i][j])

n=int(input())

for _ in range(n):
  x,y=map(int,input().split())

  for i in range(19):
    # 세로줄
    matrix[x-1][i] = 1 if matrix[x-1][i] == 0 else 0
    # 가로줄
    matrix[i][y-1] = 1 if matrix[i][y-1] == 0 else 0

# 변환된 값을 한 줄 단위로 출력
for i in range(19):
  print(*matrix[i])


