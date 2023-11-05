import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    # 총 benefit / 최대 가격
    total = max_price = 0

    # 가장 먼 미래부터 지금까지 가격 확인
    for idx in range(N-1, -1, -1):
        price = prices[idx]
        # 지금 가격이 더 비싸다면,
        if price > max_price:
            # 팔아야 하는 가격 갱신
            max_price = price
        # 지금 가격이 더 싸다면,
        else:
            # 바로 이윤 계산
            profit = max_price - price
            total += profit

    print(f'#{tc} {total}')