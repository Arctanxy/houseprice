class Solution(object):
    def islandPerimeter(self,grid):
        '''grid为二维数组，元素只有0和1,1代表岛屿，0代表水，数组中只有一个岛屿，且岛屿中没有水'''
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 4
                    if i>0:
                        if grid[i-1][j] == 1:
                            count -= 2
                    if j>0:
                        if grid[i][j-1] == 1:
                            count -= 2

        return count

s = Solution()
k = s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])

print(k)



