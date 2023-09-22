N = int(input())
arr = list(map(int,input().split()))
new_arr = sorted(set(arr)) # set은 중복 제거, sorted는 오름차순 정렬 함수

for i in new_arr: # [1,2,3,4]로 주어지는걸 1 2 3 4로 표현하기
    print(i, end=' ')