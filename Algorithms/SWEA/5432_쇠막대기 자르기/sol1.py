import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sticks = input().replace('()', '*')
    # answer: 총 막대기 개수, bar: 열린 ( 의 숫자
    answer = bar = 0

    for char in sticks:
        if char == '(':
            bar += 1
        elif char == ')':
            bar -= 1
            answer += 1
        else:  # 레이저 *
            answer += bar

    print(f'#{tc} {answer}')