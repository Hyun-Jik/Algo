T = int(input())

arr = [[0] * 100 for _ in range(100)] # 크기 100인 도화지 전부 0으로 만들어준다
for tc in range(1,T+1):
    x1, y1 = map(int,input().split())

    for i in range(x1, x1+10): # 크기 10인 정사각형 색종이의 가로
        for j in range(y1,y1+10): # 크기 10인 정사각형 색종이의 세로
            arr[i][j] = 1  # 해당하는 부분을 1로 해준다.
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1: # 100x100을 순환하면서 숫자 1로 채워진 부분이 있으면
            count +=1  # 갯수 하나를 추가해라

print(count)
