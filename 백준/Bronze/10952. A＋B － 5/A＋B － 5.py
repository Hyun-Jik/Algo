while True:
    A, B = map(int, input().split())
    if A==0 and B==0: # A와 B 둘 다 0 0 이면 빠져나올 수 있게
        break
    else:
        print(A+B)