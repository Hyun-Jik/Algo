import sys
input = sys.stdin.readline
# 입력 출력
# 속도 빠르게


N,M = map(int,input().split())
baskt = [0] * N # 바구니를 0 1 2 3 4 번호(N) <- (1 2 3 4 5 번호로 만들어줌(N+1))

for _ in range(M): # M줄에 걸쳐
    i,j,k = map(int,input().split()) # i, j, k 를 만들어냄

    for idx in range(i,j+1): # 공을 i번 자리부터 j번 자리까지 집어넣음
        baskt[idx-1] = k  # idx -1(i,j,k = 1(0) 2(1) 3 일때) 에 해당하는 위치에 k번의 공 넣는다

print(*baskt)
