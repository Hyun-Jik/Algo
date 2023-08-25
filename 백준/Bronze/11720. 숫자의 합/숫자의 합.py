N = int(input())
arr = list(map(int,input()))

sum = 0
for i in arr: # i 가 arr를 순회하면서
    sum += i  # 0에서부터 i 값들을 더한다

print(sum)