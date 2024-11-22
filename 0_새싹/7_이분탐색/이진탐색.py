def binary_search(l, r, target, cnt):
    # l과 r을 이용해서 c를 구한다
    c = int((l+r)/2)

    # c == target
    if c == target:
        # 종료조건, cnt를 리턴
        return cnt

    # c > target
    elif c > target:
        # r값을 갱신하며 재귀
        return binary_search(l, c, target, cnt+1)

    # c < target
    elif c < target:
        # l값을 갱신하며 재귀
        return binary_search(c, r, target, cnt+1)


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    cnt_A = binary_search(1, P, A, 1)
    cnt_B = binary_search(1, P, B, 1)

    ans = "A" if cnt_A < cnt_B else "B" if cnt_B < cnt_A else 0

    print(f'#{tc} {ans}')