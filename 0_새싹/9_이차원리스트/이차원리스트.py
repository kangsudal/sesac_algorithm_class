matrix = [[3, 7, 9, 10],
          [8, 1, 5, 11],
          [2, 4, 6, 12]]

# 1. 조회
print(matrix[2][1])

# 2. 순회
# 행 우선 순회
for r in range(3):
    for c in range(4):
        print(matrix[r][c])

# 열 우선 순회
for c in range(4):
    for r in range(3):
        print(matrix[r][c])

# 3. 전치
matrix = [[3, 7, 9],
          [8, 1, 5],
          [2, 4, 6]]

for r in range(3):
    for c in range(3):
        if r > c:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

print(matrix)

# zip 함수를 활용한 전치
print(list(zip(*matrix)))   # 인자로 여러개의 덩어리를 받는다