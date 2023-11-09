T = int(input())

for tc in range(1,T+1):
    grass = input()

    cnt = 0

    for i in range(len(grass)):
        if grass[i] == '(':
            if grass[i+1] == ')' or grass[i+1] == '|':
                cnt += 1
        elif grass[i] == ')':
            if grass[i-1] == '|':
                cnt +=1

    print(f'#{tc} {cnt}')