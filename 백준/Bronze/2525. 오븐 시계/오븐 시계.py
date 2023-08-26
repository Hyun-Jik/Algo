A, B = map(int,input().split())
C = int(input())

hour = (B+C) // 60 # 60분 이상을 더 하는 것에 대비
minu = (B+C) % 60

if B+ C >= 60:  # B+C가 60을 넘으면
    if A + hour >= 24:
        A =A - 24  # 시에는 해당되는만큼 //60 해준걸 더하고
    print(A+hour, minu)   # 분은 minu 만큼만 구해줌

else:   # B+C가 60보다 작으면
    if A >= 24:     # 24가 넘어가면 25부터는 1시 이므로 -24 해줌
        A =A- 24
    print(A, B+C)   # 분을 그냥 더 해주면 됨
