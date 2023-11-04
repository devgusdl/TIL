# https://www.acmicpc.net/problem/1244

# 스위치 총 개수
N = int(input())

# 스위치 초기 상태 리스트
switches = list(map(int, input().split()))

# 학생수
case = int(input())

for _ in range(case):
    # 성별, 스위치 번호
    gender, switch_no = map(int, input().split())
    # 스위치 번호 => 인덱스로 변환
    idx = switch_no - 1

    # 남학생이면
    if gender == 1:
        while idx < N:
            # 0 <=> 1
            # switches[idx] = 0 if switches[idx] else 1
            switches[idx] ^= 1

            # 처음 받은 스위치 번호만큼 점프하며 같은 작업 반복
            idx += switch_no
    # 여학생이면
    else:
        # 일단, 받은 카드번호 바꿈
        switches[idx] ^= 1
        side = 1
        # 왼쪽은 0보다 크거나 같고, 오른쪽은 N보다 작음
        while 0 <= idx - side and idx + side < N:
            # 양 옆의 값이 같다면
            if switches[idx - side] == switches[idx + side]:
                # 양옆 모두 바꿈
                switches[idx - side] ^= 1
                switches[idx + side] ^= 1
                # 한칸 더 이동
                side += 1
            # 다르다면 반복문 멈춤
            else:
                break

for line_no in range(N // 20 + 1):
    start = 20 * line_no
    end = 20 * (line_no + 1)
    # print(' '.join(map(str, switches[start:end])))
    print(*switches[start:end])

'''
41
0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 1 0
2
1 3
2 3

'''