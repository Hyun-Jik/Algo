def solution(my_string, n):
    answer = []
    for i in my_string:
        answer1 = i*n  #my_string의 각각 문자를 n번씩 곱합
        answer.append(answer1) # ["hhh","eee","lll","lll","ooo"] 값이 나옴
    return ''.join(answer)