def rotate_matrix(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


if __name__ == "__main__":
    n = int(input("Enter matrix size: "))
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = rotate_matrix(matrix)
    print("Rotated Matrix:")
    for row in result:
        print(*row)
