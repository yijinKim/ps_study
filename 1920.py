import sys
input = sys.stdin.readline

N = int(input())
an = set(map(int, input().split()))
M = int(input())
am = list(map(int, input().split()))

for m in am:
    if m in an:
        print(1)
    else:
        print(0)


import sys
input = sys.stdin.readline

N = int(input())
an = list(map(int, input().split()))
an.sort()
M = int(input())
am = list(map(int, input().split()))

for m in am:
	left = 0
	right = N - 1
	
	while left <= right:
		mid = (left + right) // 2
		if m > an[mid]:
			left = mid + 1
		elif m < an[mid]:
			right = mid - 1
		else:
			left = mid
			right = mid
			break
	if left == mid and right == mid:
		print(1)
	else:
		print(0)

