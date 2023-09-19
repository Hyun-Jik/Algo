import sys
input = sys.stdin.readline

N = int(input()) # 수의 개수 N이 주어짐
list = [int(input()) for _ in range(N)]  # N개의 줄에 숫자가 주어짐

list.sort(reverse =True) # sort() 기본 정렬은 오름차순
for i in list:
    print(i)