import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    counter = [0] * 10

    for card in cards:
        counter[card] += 1

    max_card = 0
    max_count = counter[max_card]

    for idx in range(10):
        if counter[idx] >= max_count:
            max_count = counter[idx]
            max_card = idx

    print(f'#{tc} {max_card} {max_count}')
