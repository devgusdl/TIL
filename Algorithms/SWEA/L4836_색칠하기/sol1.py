import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # matrix = [[0] * 10 for _ in range(10)]
    matrix = [[0 for _ in range(10)] for _ in range(10)]

    N = int(input())

    # N번 색칠하기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 한번 색칠하기
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                # row, col 칸이 0이 아니고(무언가 색이 칠해져 있음) and
                # 기존 색이 지금 칠하려는 색이 아니라면
                if matrix[row][col] and matrix[row][col] != color:
                    matrix[row][col] = 3
                # 색이 없거나, 기존색과 같은 색을 칠한다면, 덮어쓰기
                else:
                    matrix[row][col] = color

    # 보라색 개수 세기
    count = 0
    for r in range(10):
        for c in range(10):
            if matrix[r][c] == 3:
                count += 1

    print(f'#{tc} {count}')