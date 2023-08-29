def solution(n):
    answer = 0
    for i in str(n): # 정수를 str(문자열)로 변환 시킴
        answer += int(i) # 정수 값으로 변환시켜 각각 더함
    return answer