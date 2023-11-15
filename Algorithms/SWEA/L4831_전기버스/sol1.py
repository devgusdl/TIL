import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # K: 이동거리, N: 정류장 개수, M: 충전기 개수
    K, N, M = map(int, input().split())
    stations = [False] * (N + 1)

    chargers = list(map(int, input().split()))
    for charger in chargers:
        stations[charger] = True

    # 충전 횟수 (0)
    count = 0
    # 마지막 충전 장소 (0) idx
    last_charge = 0
    # 현재 위치 (K) idx
    current = K

    # 현재 위치가 정류장 안에 있다면
    while current < N:
        # 현재 위치가 충전소라면
        if stations[current]:
            # 1. 충전하고
            count += 1
            # 2. 마지막 충전장소 갱신
            last_charge = current
            # 3. 현재 위치 최대한 멀리 이동
            current += K

        # 현재 위치가 충전소가 아니라면
        else:
            # 한칸 앞으로 이동
            current -= 1

        # 현재 위치가 마지막 충전 장소와 같다면
        if current == last_charge:
            # 실패
            count = 0
            break

    print(f'#{tc} {count}')