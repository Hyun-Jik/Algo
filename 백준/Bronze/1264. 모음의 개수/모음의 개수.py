while True:
    sentence = input()
    cnt = 0
    #예제 입력의 3줄의 문장 후 #이 나왔을때 빠져나가도록 함
    if sentence == '#':
        break
    #모음 소문자, 모음 대문자 둘 다 세야하기 때문에
    for i in sentence:
        if i in 'aeiouAEIOU':
            cnt+=1
    print(cnt)