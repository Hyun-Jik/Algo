def solution(hp):
    answer1 = hp // 5
    answer2 = (hp % 5) // 3
    answer3 = hp % 5 % 3
    answer = answer1 + answer2 + answer3
    return answer