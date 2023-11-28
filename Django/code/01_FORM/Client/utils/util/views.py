from django.shortcuts import render
import requests

# Create your views here.
def lotto_in(request):
    return render(request, 'util/lotto_in.html')

def lotto_out(request):
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
    data = res.json()
    my_numbers = []
    real_numbers = [data[f'drwrtNo{i}'] for i in range(1, 7)]
    bonus_no = data['bnusNo']

    same_count = len(set(my_numbers) & set(real_numbers))

    if same_count == 6:
        print(1)
    elif same_count == 5 and bonus_no in my_numbers:
        print(2)
    elif same_count == 5:
        print(3)
    elif same_count == 4:
        print(4)
    elif same_count == 3:
        print(5)
        return render(request, 'util/lotto_in.html')