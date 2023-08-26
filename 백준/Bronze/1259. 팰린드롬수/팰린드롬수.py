

while True:
    n = input()

    if n == '0': # 0이면 빠져나가기
        break
    else:
        if n == n[::-1]: # 배열 방향 반대로 확인해도 같을 때
            print('yes')
        else:
            print('no')