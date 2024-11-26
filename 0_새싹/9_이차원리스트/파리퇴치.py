# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # flies를 순회하며(r, c)
    for r in range(N-M+1):
        for c in range(N-M+1):
        # 임시값을 초기화
            tmp = 0
        # (r, c)를 기준으로
            # M*M만큼 다시 순회
            for x in range(r, r+M):
                for y in range(c, c+M):
                # 임시값 더하기
                    tmp += flies[x][y]
            # 정답 갱신
            ans = max(ans, tmp)

    print(f'{tc} {ans}')