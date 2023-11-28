# client/lotto_api.py
import requests

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
data = res.json()

# 로또번호 6개
numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]
# 보너스넘버 
bonus_no = data['bnusNo']



print(numbers, bonus_no)