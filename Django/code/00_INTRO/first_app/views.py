from django.shortcuts import render

from django.http import HttpResponse

import random

# /hello/
def hello(request):
    return render(request, 'hello.html')


def bye(request):
    # bye.html 을 렌더하도록 하자.
    # 파일 안에는 적당히 h1, p 내용 쓰기
    return render(request, 'bye.html')


def lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()
    context = {
        'message': '부자되고싶다',
        'lucky_numbers': lucky_numbers,
    }
    
    return render(request, 'lotto.html', context)

# /lunch/ => lunch view function => 여러 메뉴들 중에 하나 뽑아서 => 사용자에게 lunch.html 로 보여줌
def lunch(request):
    menus = ['짜장면', '치킨', '순대국', '피자', '백반', '샐러드', '간헐적단식']
    menu = random.choice(menus)
    
    return render(request, 'lunch.html', {
        'menu': menu,
    })