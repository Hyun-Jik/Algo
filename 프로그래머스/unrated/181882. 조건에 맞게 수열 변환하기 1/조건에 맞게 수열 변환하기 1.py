def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(int(i / 2))
        elif i < 50 and i % 2 == 1:
            answer.append(i * 2)
        else:
            answer.append(i)
    #answer.append(i)를 한번에 쓰면 왜 안 되는지?
    return answer
