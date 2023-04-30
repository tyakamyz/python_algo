# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque

def binaryMatrix(graph):
    n = len(graph)
    if graph[0][0] == 1 or graph[n-1][n-1] == 1:
        return -1
    elif n == 1:
        return 1
    
    visited = [[False]*n for _ in range(n)]

    r = [-1, 1, 0, 0, -1, -1, 1, 1]
    c = [0, 0, -1, 1, -1, 1, -1, 1]
    
    def bfs():
        x=0
        y=0
        visited[x][y] = True
        que = deque()
        que.append((x,y,1))

        result = -1

        while que:
            currentX, currentY, currentLen = que.popleft()

            if currentX == n-1 and currentY == n-1:
                 result = currentLen
                 break

            for i in range(8):
                x = currentX + r[i]
                y = currentY + c[i]

                if ((x >= 0 and x < n) and (y >= 0 and y < n)):
                        if (graph[x][y] == 0 and not visited[x][y]):
                            visited[x][y] = True
                            que.append((x,y,currentLen+1))
        
        return result
    
    return bfs()

print(binaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))