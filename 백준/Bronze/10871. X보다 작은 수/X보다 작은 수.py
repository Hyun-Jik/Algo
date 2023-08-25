N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in A: # i는 A라는 수열을 돈다
    if X > i: # i 값이 x 보다 작으면
        print(i, end=' ') # 작은 값들을 출력한다