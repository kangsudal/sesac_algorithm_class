import sys
input = sys.stdin.readline

n = int(input().strip())
in_out_log = []

for _ in range(n):
    my_log = input().split()
    if my_log[1] ==  'enter':
        in_out_log.append(my_log[0])
    else:
        in_out_log.remove(my_log[0])

in_out_log.sort(reverse=True)

for person in in_out_log:
    print(person)