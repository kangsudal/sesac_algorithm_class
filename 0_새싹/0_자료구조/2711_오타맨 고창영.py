T = int(input())

for _ in range(T):
    idx, word = input().split()
    idx = int(idx)-1

    print(word[:idx] + word[idx+1:])

#####################################

T = int(input())

for _ in range(T):
    idx, word = input().split()
    idx = int(idx)-1
    word = list(word)
    word.pop(idx)

    print(''.join(word))