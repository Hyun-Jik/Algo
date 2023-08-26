
while True:
    try:    # try 안의 코드를 시도해봐라
        A, B = map(int,input().split())
        print(A+B)
    except: # try 코드 실행되지않을때 except의 명렁어를 수행해라
        break