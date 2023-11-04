import sys
sys.stdin = open('input.txt')


def solution(matrix):
    # 아래 => 위
    direction = 'U'
    # 시작하는 행(줄) idx
    row = 99
    col = matrix[row].index(2)

    # 맨 첫줄(row=0)까지 반복
    while row > 0:
        # 올라가는 도중에는,
        if direction == 'U':
            # 오른쪽(col+1)을 주시하기
            if col < 99 and matrix[row][col+1]:
                direction = 'R'
                col += 1
            # 왼쪽(col-1)을 주시하기
            elif col > 0 and matrix[row][col-1]:
                direction = 'L'
                col -= 1
            # 왼/오 모두 갈 수 없으면,
            else:
                row -= 1

        # 좌우 이동 중에는,
        else:
            # 위(row-1)를 주시하기
            if matrix[row-1][col]:
                direction = 'U'
                row -= 1
            elif direction == 'L':
                col -= 1
            elif direction == 'R':
                col += 1

    return col


T = 10

for _ in range(T):
    tc = input()
    matrix = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{tc} {solution(matrix)}')  # 시작점 col 번호