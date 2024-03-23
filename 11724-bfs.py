from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

N, M = map(int ,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
cnt = 0

visited = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)