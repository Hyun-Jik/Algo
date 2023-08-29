num_list = []   # num_list에 빈 array 넣기
for i in range(9):  # 9번 반복
    num_list.append(int(input()))   # num_list에 append 해줌 

print(max(num_list))
print(num_list.index(max(num_list))+1)  # 리스트에 x 있으면 x 위치 값, 문제는 1부터 시작하므로 +1 
