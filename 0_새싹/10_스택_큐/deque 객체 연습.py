from collections import deque

queue = deque([3, 5, 1, 4, 2])  # 리스트로 감싸서 넣어줄 것!
queue.append(100)
print(queue)
num = queue.popleft()
print(num, queue)