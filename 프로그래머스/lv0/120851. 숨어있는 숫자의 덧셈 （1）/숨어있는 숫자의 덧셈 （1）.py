def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit(): # isdecimal(), isdigit(), isnumeric() : 주어진 문자열이 숫자로 되어있는지 검사하는 함수
            answer += int(i) # 나온 숫자 형태의 문자열을 숫자로 변환 후 더해줌
    return answer