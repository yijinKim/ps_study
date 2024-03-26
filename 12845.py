import sys
input = sys.stdin.readline

n = int(input())
levels = list(map(int, input().split()))
levels.sort(reverse=True)

maxLevel = levels[0]
print(maxLevel*(n-1) + sum(levels[1:]))