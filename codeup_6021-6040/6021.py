# https://codeup.kr/problem.php?id=6021
# 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기

# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

a = input()

for i in range(len(a)):
    print(a[i])

# 문자열을 for문으로 사용하는 경우, 글자 각각 for문이 돌아간다.
for i in a:
    print(i)