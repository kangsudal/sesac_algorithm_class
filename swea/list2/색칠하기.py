# import sys
# input = sys.stdin.readline

sheet = [[0] * 10 for _ in range(10)]

def get_amount_of_cells_overlapping():
    amount_of_cells = 0
    for r in range(10):
        for c in range(10):
            if sheet[r][c] == -1:
                amount_of_cells += 1
    # for r in range(10):
    #     print(sheet[r])
    return amount_of_cells

def fill_cells(r1,c1,r2,c2,color):
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            # 색칠이 아직 안돼있거나 같은색이면 그대로 색을 칠한다(같은 색인 영역은 겹치지 않는다.)
            if sheet[r][c] == 0 or sheet[r][c] == color:
                sheet[r][c] = color
            #겹친 영역은 -1로 색칠한다
            else:
                sheet[r][c] = -1

T = int(input())

for test_case in range(T):
    # 매 테스트 케이스마다 sheet 초기화
    sheet = [[0] * 10 for _ in range(10)]
    N = int(input())
    for n in range(N):
        r1,c1,r2,c2,color = map(int,input().split())
        fill_cells(r1,c1,r2,c2,color)
    print(f'#{test_case + 1} {get_amount_of_cells_overlapping()}')

