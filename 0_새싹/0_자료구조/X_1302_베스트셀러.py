import sys
input = sys.stdin.readline

N = int(input())
book_sales = dict()

for _ in range(N):
    book_name = input().rstrip()

    # 키값이 존재하지 않는 경우
    if book_name not in book_sales:
        # 새로 생성(book_name : 1)
        book_sales[book_name] = 1

    # 키값이 존재하는 경우
    else:
        # += 1
        # book_sales[book_name] = book_sales[book_name] + 1
        book_sales[book_name] += 1


# 가장 많이 팔린 책 찾기

# 1. 선형탐색
# 초기값 설정
max_sales = 0
max_sales_book = ''
# 딕셔너리를 선형탐색하면서
for book, cnt in book_sales.items():
    # 만약 그 책이 max_sales보다 많이 팔렸다면?
    if cnt > max_sales:
        # max_sales_book, max_sales 갱신
        max_sales_book = book
        max_sales = cnt

    # 만약 똑같이 팔렸다면?
    elif cnt == max_sales and book < max_sales_book:
        # 더 작은 책 제목으로 갱신
        max_sales_book = book
print(max_sales_book)


# 2. 딕셔너리 정렬
sorted_sales_info = sorted(book_sales.items(), key=lambda x: (-x[1], x[0]))
print(sorted_sales_info[0][0])