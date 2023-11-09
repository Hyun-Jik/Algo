T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
 
    score = []
    for i in range(N):
        A, B, C = map(int, input().split())
        total = (A*0.35)+(B*0.45)+(C*0.2)
        score.append(total)
 
    K_score = score[K-1]
    score.sort(reverse=True)
    number = score.index(K_score)//(N//10)
 
    print(f'#{test_case} {grade[number]}')