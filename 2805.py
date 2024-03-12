import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

min_h, max_h = 1, max(trees)
while min_h <= max_h:
    sum_m = 0
    mid_h = (min_h + max_h) // 2
    for tree in trees:
        if tree >= mid_h:
            sum_m += (tree-mid_h)
        if sum_m >= M:
            break
    if sum_m >= M:
        min_h = mid_h + 1
    else:
        max_h = mid_h - 1
print(max_h)