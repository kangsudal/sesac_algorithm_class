T = int(input())

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 이차원리스트 패딩
    matrix = [[0]*(N+2) for _ in range(M+2)]
    for i in range(1, N+1):
        matrix[i][1:M+1] = list(map(int, input().split()))

    ans = 0

    # matrix를 순회하며,
    for r in range(1, N+1):
        for c in range(1, M+1):
        # 기준이 되는 r, c에서
            # 임시값 갱신
            tmp = matrix[r][c]
            # 4방향 델타탐색
            for d in range(4):
                # 새로운 좌표를 찍어보고
                nr, nc = r+dr[d], c+dc[d]
                # 임시값 구하기
                tmp += matrix[nr][nc]
            # 정답 갱신
            ans = max(ans, tmp)

    print(f'{tc} {ans}')