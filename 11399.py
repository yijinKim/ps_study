import sys
input = sys.stdin.readline

N = int(input())
answer = list(map(int, input().split()))
answer.sort()

for i in range(1, N):
    answer[i] += answer[i-1]

print(sum(answer))