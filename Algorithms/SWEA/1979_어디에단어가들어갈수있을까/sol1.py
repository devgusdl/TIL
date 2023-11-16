import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzles = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        # 단어의 길이를 카운트 해준다.
        word_length = 0
        for j in range(N):
            if puzzles[i][j] == 1:
                # 흰 색일 경우 단어의 길이 + 1
                word_length += 1
            # 검정색일 경우 혹은 칸의 마지막일 경우에
            if puzzles[i][j] == 0 or j == N - 1:
                # 단어의 길이가 K라면 단어가 들어갈 횟수 + 1
                if word_length == K:
                    count += 1
                word_length = 0

        for j in range(N):
            # 위와 동일하지만 i,j를 바꿔서 실행. 행도 살펴보고 열도 살펴보고
            if puzzles[j][i] == 1:
                word_length +=1
            if puzzles[j][i] == 0 or j == N - 1:
                if word_length == K:
                    count += 1
                word_length = 0

    print(f'#{tc} {count}')