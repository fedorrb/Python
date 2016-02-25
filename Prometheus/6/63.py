def saddle_point(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return (0,0)
    def get_min_elem(mat):
        is_min = True
        min_pos = 0
        curr_pos = 1
        min = mat[0]
        while curr_pos < len(mat):
            if mat[curr_pos] < min:
                min = mat[curr_pos]
                min_pos = curr_pos
            elif mat[curr_pos] == min:
                is_min = False
                break
            curr_pos = curr_pos + 1
        if is_min:
            return min_pos
        else:
            return False
    y = 0
    x_pos = 0
    y_pos = 0
    y_val = 0
    found = False
    while y < len(matrix):
        x_pos = get_min_elem(matrix[y])
        if x_pos != False:
            y_val = matrix[y][x_pos]
            y_pos = 0
            found = True
            while y_pos < len(matrix):
                if y_pos == y:
                    y_pos = y_pos + 1
                    continue
                if matrix[y_pos][x_pos] >= y_val:
                    found = False
                    break
                y_pos = y_pos + 1
        if found:
            break
        y = y + 1
    if found and x_pos != False:
        return (y, x_pos)
    else:
        return False
def saddle_point1(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            flag = True
            ii = 0
            jj = 0
            for ii in range(len(matrix)):
                if matrix[ii][j] >= matrix[i][j] and i != ii:
                    flag = False
            for jj in range(len(matrix[i])):
                if matrix[i][jj] <= matrix[i][j] and j != jj:
                    flag = False
            if flag:
                return (i, j)
    return False
matrix1 = [[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]
#matrix1 = [[21]]
#matrix1 = [[1,2,3],[3,2,1]]
#matrix1 = [[1,2,3,0,1,1],[4,3,2,1,1,2],[4,3,2,0,1,1],[0,0,0,0,0,1]]
#matrix1 = [[0,0,0],[2,1,2],[1,0,1]]
print saddle_point(matrix1)