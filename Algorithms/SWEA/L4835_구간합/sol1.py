import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = min_sum = sum(numbers[:M])

    for start in range(N-M+1):
        end = start + M
        total = sum(numbers[start:end])

        if total > max_sum:
            max_sum = total

        if total < min_sum:
            min_sum = total

    ans = max_sum - min_sum
    print(f'#{tc} {ans}')