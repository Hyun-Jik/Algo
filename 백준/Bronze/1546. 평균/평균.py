N = int(input())
arr = list(map(int,input().split()))
max_score = max(arr)

alist = [] # 빈 리스트 만들어주기
for i in arr:
    alist.append(i/max_score * 100) # 새로운 계산 값 만들어 주고 리스트로 만들기
new_avg = sum(alist)/N  # 새로운 계산 값들의 평균 구하기
print(new_avg)
