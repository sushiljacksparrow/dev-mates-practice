dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def island(grid, temp, i, j, t, l, m):
    temp[i][j] = 1
    count = t
    for x in enumerate(dir):
            if i + dir[x][0] >=0 and i + dir[x][0] < l and j + dir[x][1] >= 0 and j + dir[x][1] < m:
                if temp[i + dir[x][0]][j + dir[x][1]] == 0 and grid[i + dir[x][0]][j + dir[x][1]] == 1:
                    count = max(count, island(grid, temp, i + dir[x][0], j + dir[x][1], t + 1, l, m))
    return count

if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    l = len(grid)
    m = len(grid[0])
    res = 0
    temp = [[0 for x in range(m)] for y  in range(l)]
    for i in range(l):
        for j in range(m):
            if grid[i][j] == 0 and temp[i][j] == 0:
                res = max(res, island(grid, temp, i , j, 1, l, m))

    print(res)
