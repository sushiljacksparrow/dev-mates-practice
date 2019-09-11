
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def flood_fill(image, temp, sr, sc, start_color, new_color):
    temp[sr][sc] = 1
    image[sr][sc] = new_color
    for i in range(4):
        if sr + dir[i][0] >=0 and sr + dir[i][0] < len(image) and sc + dir[i][1] >=0 and sc + dir[i][1] < len(image[1]):
            if not temp[sr + dir[i][0]][sc + dir[i][1]] and image[sr + dir[i][0]][sc + dir[i][1]] == start_color:
                flood_fill(image, temp, sr + dir[i][0], sc + dir[i][1], start_color, new_color)



if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    sr = 1
    sc = 1
    new_color = 2
    temp = [[0 for x in range(len(image[0]))] for y in range(len(image))]

    flood_fill(image, temp, sr, sc, image[sr][sc], new_color)
