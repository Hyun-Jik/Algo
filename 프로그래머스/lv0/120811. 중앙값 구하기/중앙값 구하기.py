def solution(array):
    array.sort()
    answer = array[len(array)//2] # len(array)//2 : 총 길이의 가운데 값
    return answer