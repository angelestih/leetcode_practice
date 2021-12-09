from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(heights)
        n = len(heights[0])
        #to track whether atlantic and/or pacific water reaches the cell
        atlantic_reach = [[False for _ in range(n)] for _ in range(m)]
        pacific_reach = [[False for _ in range(n)] for _ in range(m)]

        result = []

        for row in range(m):
            #when starting from the top left, the corner will always be reachable by the pacific ocean
            self.dfs(row, 0, pacific_reach, m, n, heights)
            #when starting from the top right, the corner will always be reachable by the atlantic ocean
            self.dfs(row, n-1, atlantic_reach, m, n, heights)

        for column in range(n):
            #when starting from the top left, the corner will always be reachable by the pacific ocean
            self.dfs(0, column, pacific_reach, m, n, heights)
            #when starting from the top right, the corner will always be reachable by the atlantic ocean
            self.dfs(m - 1, column, atlantic_reach, m, n, heights)

        for row in range(m):
            for column in range(n):
                if pacific_reach[row][column] == True and atlantic_reach[row][column] == True:
                    #add the cells that are reached by both oceans to the result list
                    result.append([row,column])
        return result


    def dfs(self, row, column, ocean, rows_number, columns_number, heights):
        ocean[row][column] = True
        #cell can be reached if it's being checked
        for direction in self.directions:
            next_row = row + direction[0]
            next_column = column + direction[1]
            if next_row < 0 or next_row >= rows_number or next_column < 0 or next_column >= columns_number or ocean[next_row][next_column] == True or heights[next_row][next_column] < heights[row][column]:
                #skip wrong coordinates and case when next cell is smaller than current cell
                #because we are looking from outward towards inward
                continue
            #check next cell
            self.dfs(next_row, next_column, ocean, rows_number, columns_number, heights)

