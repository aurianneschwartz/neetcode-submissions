from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        counter = 0
        nb_fruit = 0
        rotten = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] != 0:   
                    nb_fruit += 1

        while len(rotten) != 0:
            for _ in range(len(rotten)):
                current = rotten.popleft()
                nb_fruit -= 1
                if 0<=current[0]+1<len(grid) and grid[current[0]+1][current[1]] == 1:
                    rotten.append((current[0]+1,current[1]))
                    grid[current[0]+1][current[1]] = 3
                if 0<=current[0]-1<len(grid) and grid[current[0]-1][current[1]] == 1:
                    rotten.append((current[0]-1,current[1]))
                    grid[current[0]-1][current[1]] = 3
                if 0<=current[1]+1<len(grid[0]) and grid[current[0]][current[1]+1] == 1:
                    rotten.append((current[0],current[1]+1))
                    grid[current[0]][current[1]+1] = 3
                if 0<=current[1]-1<len(grid[0]) and grid[current[0]][current[1]-1] == 1:
                    rotten.append((current[0],current[1]-1))
                    grid[current[0]][current[1]-1] = 3
            if len(rotten) != 0:
                counter+=1

        if nb_fruit != 0:
            return -1
        
        return counter
