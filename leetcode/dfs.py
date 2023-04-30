# https://leetcode.com/problems/keys-and-rooms/

from collections import deque

def canVisitAllRooms(rooms):
    visited = set()

    def dfs(currentV):
        visited.append(currentV)

        for v in rooms[currentV]:
            if v not in visited:
                dfs(v)

    def bfs(startV):
        que = deque()
        que.append(startV)
        visited.add(startV)

        while que:
            currentV = que.popleft()
            
            for v in rooms[currentV]:
                if v not in visited:
                    que.append(v)
                    visited.add(v)

    #dfs(0)
    bfs(0)

    if len(visited) == len(rooms):
        return True
    
    return False

print(canVisitAllRooms([[1,3], [2,4], [0], [4], [], [3,4]]))