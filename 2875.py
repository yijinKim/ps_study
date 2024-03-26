import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cnt = 0
while n >=2 and m >= 1:
    n -= 2
    m -= 1
    if n+m >= k:
        cnt += 1
    else:
        break
print(cnt)