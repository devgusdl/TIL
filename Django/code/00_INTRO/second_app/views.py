from django.shortcuts import render
from datetime import datetime
# fibo는 피보나치 수열 10개를 fibo.html에서 사용자에게 보여줌 (ul > li) 
def fibo(request):
    fibo_numbers = [1, 1]
    for _ in range(8):
        x, y = fibo_numbers[-1], fibo_numbers[-2]
        fibo_numbers.append(x + y)

    return render(request, 'fibo.html', {
        'fibo_numbers': fibo_numbers,
    })


# is_xmas 함수는 오늘이 크리스마스라면 YES를 아니라면 NO 를 is_xmas.html에서 보여줌 (datetime 모듈 검색) 
def is_xmas(request):
    today = datetime.now()
    checker = datetime(2023, 12, 25)

    # result = 'YES' if today.month == checker.month and today.day == checker.day else 'NO'
    if today.month == checker.month and today.day == checker.day:
        result = 'YES'
    else:
        result = 'NO'

    return render(request, 'is_xmas.html', {
        'result': result,
    })