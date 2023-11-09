T = int(input())

for tc in range(1,T+1):
    N = int(input())
    k = 1
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    while True:
        num = str(k*N)
        for i in num:
            if i in numbers:
                numbers.remove(i)
        if not numbers:
            break
        k+=1
    print(f'#{tc} {num}')