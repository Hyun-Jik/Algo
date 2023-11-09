T = int(input())

for tc in range(1, T+1):
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    N, K = map(int, input().split())
    score = [] # 빈 숫자 리스트

    for _ in range(N): # 첫번째 케이스(10명) 처럼 10명에 대해서
        M, F, H = map(int,input().split()) # 중간, 기말, 과제 점수가 부여됨
        total = (M*0.35) + (F*0.45) + (H*0.2) # 각 숫자 들의 총점 구하기
        score.append(total) # 계산된 총점을 붙여줌 - list로 나타날 것

    K_score = score[K-1]
    score.sort(reverse=True)
    number = score.index(K_score)

    print(f'#{tc} {grade[number//(N//10)]}')