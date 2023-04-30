# https://leetcode.com/problems/keys-and-rooms/

def canVisitAllRooms(rooms):
    visited = []

    def dfs(currentV):
        visited.append(currentV)

        for v in rooms[currentV]:
            if v not in visited:
                dfs(v)

    dfs(0)

    if len(visited) == len(rooms):
        return True
    
    return False

print(canVisitAllRooms([[1,3], [2,4], [0], [4], [], [3,4]]))