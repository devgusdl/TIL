import sys
# 앞으로 입력(input())은 'input.txt' 에서 가져오겠다!
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # [477162, 658880, 751280, 927930, 297191]
    numbers = list(map(int, input().split()))

    # answer = max(numbers) - min(numbers)  # O(2n) => O(n)

    max_val = min_val = numbers[0]

    for num in numbers:   # O(n)
        if num >= max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    answer = max_val - min_val

    print(f'#{tc} {answer}')