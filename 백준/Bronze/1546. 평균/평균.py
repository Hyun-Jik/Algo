N = int(input())
mylist = list(map(int,input().split()))

# 점수들의 합 *100 / 최대 점수 / 점수 갯수 로 구해야 한다
mymax=max(mylist)  # 최대 점수
mysum=sum(mylist)  # 점수들의 합

print(mysum*100/mymax/int(N))