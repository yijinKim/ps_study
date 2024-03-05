import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
q = deque()
answer = []
for i in range(1, N+1):
    q.append(i)
cnt = 0
while q:
    num = q.popleft()
    if cnt == M-1:
        answer.append(num)
        cnt = 0
    else:
        q.append(num)
        cnt += 1
print("<%s>" %(", ".join(map(str, answer))))