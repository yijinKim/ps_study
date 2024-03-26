import sys
input = sys.stdin.readline

n, m =  map(int, input().split())

if n == 1:
    cnt = 1
elif n == 2:
    if m < 7:
        cnt = (m+1) // 2
    else:
        cnt = 4
else:
    if m >= 7:
        cnt = m - 2
    elif 4 < m < 7:
        cnt = 4
    else:
        cnt = m
print(cnt)