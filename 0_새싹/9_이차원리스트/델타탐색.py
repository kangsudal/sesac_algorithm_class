# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

matrix = [[3, 7, 9],
          [8, 1, 5],
          [2, 4, 6]]

# 초기세팅(내 위치)
r, c = 0, 2

# 4가지 방향을 한 번씩 확인하며
for d in range(4):
    # 새로운 좌표를 찍어본다
    nr, nc = r+dr[d], c+dc[d]

    # 해당 좌표가 유효한지 검사
    if 0 <= nr < 3 and 0 <= nc < 3:
        print(matrix[nr][nc])