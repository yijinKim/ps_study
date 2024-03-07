import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cnt = 0
    for i in input():
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
    