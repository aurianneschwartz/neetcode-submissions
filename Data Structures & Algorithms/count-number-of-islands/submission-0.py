class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        compteur = 0
        
        def search(x,y):

            if grid[x][y] == "0":
                return      
            grid[x][y] = "0"

            for dx in [-1, 1]:

                if 0<=x+dx<len(grid):
                    search(x+dx,y)

                if 0<=y+dx<len(grid[0]):
                    search(x,y+dx)

        for i in range(len(grid)):
            for j in range(len(grid[0])): 

                if grid[i][j] == "1":
                    search(i,j)
                    compteur += 1
          
        return compteur 

        



