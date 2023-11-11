import sys

sys.stdin = open('./input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N개의 상자, Q번의 상자 변경 횟수
    N, Q = map(int, input().split())

    # 숫자가 0인 box를 N개 배치
    box_lst = [0] * N
    # 변환할 수의 범위는 1에서 Q까지이다.
    for i in range(1, Q + 1):
        # L,R 을 받았을 때, L - 1부터 R까지의 범위를 i로 바꿔준다

        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box_lst[j] = i
    # box_list를 변환
    boxes = ' '.join(map(str, box_lst))

    print(f'#{tc} {boxes}')