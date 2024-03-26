import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
cnt = 0
i = 0

while K > 0:
    if coins[i] <= K:
        cnt += K // coins[i]
        K %= coins[i]
    i += 1

print(cnt)