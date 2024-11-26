# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYlGU56XOkDFARc
T = int(input())

# 델타 세팅
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # matrix = []
    # for _ in range(N):
    #     my_lst = list(map(int, input().split()))
    #     matrix.append(my_lst)
    ans = 0
    # matrix를 순회하며,
    for r in range(N):
        for c in range(M):
        # 기준이 되는 r, c에서
            # 임시값 갱신
            tmp = matrix[r][c]
            # 4방향 델타탐색
            for d in range(4):
                # 새로운 좌표를 찍어보고
                nr, nc = r+dr[d], c+dc[d]
                # 유효한 좌표인지 검토
                if 0 <= nr < N and 0 <= nc < M:
                    # 임시값 구하기
                    tmp += matrix[nr][nc]
            # 정답 갱신
            ans = max(ans, tmp)

    print(f'{tc} {ans}')