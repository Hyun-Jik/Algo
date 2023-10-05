import sys

N, P = list(map(int,sys.stdin.readline().split()))
W, L, G = list(map(int,sys.stdin.readline().split()))
win =[]
lose = []

for i in range(P):
    name, result = input().split()
    if result == 'W':
        win.append(name)
    else:
        lose.append(name)

score = 0
for j in range(N):
    N = input()
    if N in win:
        score += W
    else:
        if score - L >= 0:
            score -= L
        else:
            score = 0

    if score >= G:
        print("I AM NOT IRONMAN!!")
        quit()
else:
    print("I AM IRONMAN!!")