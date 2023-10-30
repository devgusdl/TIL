# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    mid = total // num
    r = num // 2

    if num % 2:
        s, e = mid - r, mid + r + 1
    else:
        s, e = mid - r + 1, mid + r + 1

    return list(range(s, e))


print(solution(3, 12))  # [3, 4, 5]
print(solution(5, 15))  # [1, 2, 3, 4, 5]
print(solution(4, 14))  # [2, 3, 4, 5]
print(solution(5, 5))  # [-1, 0, 1, 2, 3]