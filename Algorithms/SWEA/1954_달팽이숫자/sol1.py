import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    # delta: 우  하  좌  상
    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    # delta idx
    direction = 0

    # 현재 좌표값(시작위치 => 0, 0)
    row = col = 0
    # num => 앞으로 채울 숫자
    num = 1
    # 첫 칸 숫자는 채우고 시작
    matrix[row][col] = num

    # num 은 앞으로 채울 숫자
    while num != N ** 2:
        # 새로운 row/col 좌표값 생성
        new_row = row + d_rows[direction]
        new_col = col + d_cols[direction]

        # 새로운 좌표값은 0 이상 N 미만 and 채우려는 칸이 비어있어야(0) 한다.
        if 0 <= new_row < N and 0 <= new_col < N and matrix[new_row][new_col] == 0:
            # 다음 숫자로 바꿈
            num += 1
            # 현재의 좌표값을 새로운 좌표값으로 갱신한다.
            row, col = new_row, new_col
            # 새로운 좌표값에 num을 채운다.
            matrix[row][col] = num
        # 위 조건을 만족하지 않으면 (idx 범위 바깥이거나, 기존에 값이 있는 칸이라면)
        else:
            # delta 방향(direction) 을 조정한다.
            direction = (direction + 1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*matrix[i])