N = int(input())
dungchi = [] # 덩치를 빈 리스트로 받음

for tc in range(1, N+1):
    x,y = map(int,input().split())
    dungchi.append((x, y)) # 덩치들의 값을 리스트로 추가함

for i in dungchi:
    cnt = 1 # 덩치 등수는 1등부터 시작하므로
    for j in dungchi:
        if i[0] < j[0] and i[1] < j[1]: # 자신 보다 키, 몸무게 둘 다 더 크다면
            cnt += 1 # 등수를 +1 해준다

    print(cnt, end=' ')
