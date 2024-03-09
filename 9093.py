import sys
input = sys.stdin.readline

for _ in range(int(input())):
    words = input().split() # i am happy -> ["i", "am", "happy"]
    for word in words:
        print(word[::-1], end=' ')
    print()
    