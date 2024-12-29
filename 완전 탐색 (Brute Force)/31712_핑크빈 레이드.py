import sys
input = sys.stdin.readline

cool_u, damage_u = map(int,input().rstrip().split())
cool_d, damage_d = map(int,input().rstrip().split())
cool_p, damage_p = map(int,input().rstrip().split())
H = int(input().rstrip())

seconds = 0
# H>=0이 아니라 H>0.
while H>0:
    if seconds == 0 :
        H -= (damage_u+damage_d+damage_p)
    else:
        if seconds % cool_u == 0:
            H -= damage_u
        if seconds % cool_d == 0:
            H -= damage_d
        if seconds % cool_p == 0:
            H -= damage_p
    seconds += 1

print(seconds-1)