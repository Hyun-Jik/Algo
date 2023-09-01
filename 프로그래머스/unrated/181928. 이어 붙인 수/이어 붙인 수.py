def solution(num_list):
    answer = 0
    answer1 = ''
    answer2 = ''
    for i in num_list:
        if i % 2 == 0:
            answer1 = answer1 +str(i)
        if i % 2 == 1:
            answer2 = answer2 +str(i)
    answer = int(answer1) + int(answer2)
    return answer