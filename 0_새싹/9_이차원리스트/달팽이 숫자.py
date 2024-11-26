T = int(input())

# 델타 세팅(우-하-좌-상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    # N*N 0으로 가득찬 이차원 리스트 제작
    snail = [[0] * N for _ in range(N)]

    # 출발좌표 = 0, 0
    # 출발방향 = 0
    r, c, d = 0, 0, 0

    # 1 ~ N*N 까지 반복
    for num in range(1, N*N+1):
        # 현재 좌표 r, c에 숫자를 입력
        snail[r][c] = num

        # 다음 좌표를 찍어보기
        nr, nc = r+dr[d], c+dc[d]

        # 유효성 검사(범위 + 방문 여부)
        if 0 <= nr < N and 0 <= nc < N and not snail[nr][nc]:
            # 유효하다면? => 이동(r, c = nr, nc)
            r, c = nr, nc

        # 유효하지 않다면?
        else:
            # 방향 전환(0 - 1 - 2 - 3 - 0 - 1 - 2 - 3 - 0)
            d = (d+1) % 4
            # 새로운 방향을 가지고 이동
            r, c = r+dr[d], c+dc[d]

    print(f'#{tc}')
    for row in snail:
        print(*row)