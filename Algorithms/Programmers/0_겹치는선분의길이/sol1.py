# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    # 1차원 평면은 -100 ~ 100 임
    # 보정으로 0 ~ 200 의 인덱스를 갖는 리스트로 표현 가능
    # 아직 선이 지나지 않으므로 모두 0
    numbers = [0 for _ in range(201)]  # 0 ~ 200

    for line in lines:
        # 이때 lines 의 시작 끝값을 보정 (+100)
        start, end = line[0] + 100, line[1] + 100

        # lines 를 순회하며
        for idx in range(start, end):
            # 선이 지나가면 +1 을 해줌
            numbers[idx] += 1

    # 모든 선의 표시를 끝내고
    # 다시 처음부터 평면을 순회하며 겹치는(1이상) 구간을 카운트 함
    answer = 0
    for num in numbers:
        if num >= 2:
            answer += 1

    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))  # 2
print(solution([[-1, 1], [1, 3], [3, 9]]))  # 0
print(solution([[0, 5], [3, 9], [1, 10]]))  # 8