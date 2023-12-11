from django.shortcuts import render
from datetime import datetime
import requests

def index(request):
    return render(request, 'util/index.html')


def time(request):
    now = datetime.now()
    return render(request, 'util/time.html', {
        'now': now,
    })

def lotto_in(request):
    return render(request, 'util/lotto_in.html')


def lotto_out(request):
    # 사용자 input 데이터
    my = []
    # 실제 당첨번호 6개
    real = []

    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
    data = res.json()

    for i in range(1, 7):
        num = request.GET[f'num{i}']
        my.append(int(num))
        real.append(data[f'drwtNo{i}'])
    
    bonus = data['bnusNo']
    same = list(set(my) & set(real))
    # 번호 수집 완료. 등수 체크 시작
    same_count = len(same)
    if same_count == 6:
        result = '1등'
    elif same_count == 5 and bonus in my:
        result = '2등'
    elif same_count == 5:
        result = '3등'
    elif same_count == 4:
        result = '4등'
    elif same_count == 3:
        result = '5등'
    else:
        result = '꽝..'

    return render(request, 'util/lotto_out.html', {
        'my': my,
        'real': real,
        'bonus': bonus,
        'result': result,
        'same': same,
    })