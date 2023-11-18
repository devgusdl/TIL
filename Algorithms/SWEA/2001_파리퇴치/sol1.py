import sys

sys.stdin = open('input.txt')


# 파리채 한번 휘둘렀을 때의 총 합
def hit(r_idx, c_idx, size):
    total = 0
    for r in range(size):
        for c in range(size):
            total += matrix[r_idx + r][c_idx + c]

    return total


T = int(input())

for tc in range(1, T + 1):
    # N: 전체 행렬 크기, M: 파리채 크기
    N, M = map(int, input().split())
    # matrix = []
    # for _ in range(N):
    #     matrix.append(list(map(int, input().split())))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최대/최소 초기값 설정 => 최대는 가장 작은 값으로. 최소는 가장 큰 값으로
    max_val = -float('INF')  # 0으로도 설정

    for row in range(N - M + 1):
        for col in range(N - M + 1):
            # row, col 은 파리채의 시작(좌상단) idx
            '''
            total = 0
            for r in range(M):
                for c in range(M):
                    total += matrix[row+r][col+c]
            if total > max_val:
                max_val = total
            '''
            total = hit(row, col, M)  # => 내리쳤을 때 잡은 파리 수를 return
            if total > max_val:
                max_val = total

    print(f'#{tc} {max_val}')