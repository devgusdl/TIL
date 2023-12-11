my = [1, 2, 3, 4, 5, 7]

real = [1, 2, 3, 4, 5, 6]
bonus = 7

# 1등 => my 와 real이 6개 같음
# 2등 => my 와 real이 5개 같음 + my의 나머지 하나가 bonus
# 3등 => my 와 real이 5개 같음
# 4등 => my 와 real 이 4개 같음
# 5등 => 3개 같음

same_count = 0
for x in my:
    for y in real:
        if x == y:
            same_count += 1
            break

my = [1, 2, 3, 4, 5, 7]

real = [1, 2, 3, 4, 5, 6]
bonus = 7

same_count = len(set(my) & set(real))

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
