def solution(num_list):
    answer = []
    answer1 = 0
    answer2 = 0
    for i in num_list:
        if i % 2 == 0:
            answer1 += 1
        else:
            answer2 += 1
    answer = [answer1, answer2]
    return answer