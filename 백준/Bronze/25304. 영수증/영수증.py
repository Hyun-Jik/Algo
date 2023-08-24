X = int(input())
N = int(input())
sum = 0

for tc in range(1, N+1):
    a, b = map(int, input().split())
    sum += a*b

if sum == X:    # 조건문에 따른 결과가 여러개 나오는 것이 아니므로
    print('Yes')    # for문 밑에 두지 않는다
else:
    print('No')