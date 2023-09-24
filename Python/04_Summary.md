# Control_Statement (제어문)
## Conditional Statement (조건문)

if 문은 반드시 참/거짓을 판단할 수 있는 조건과 함께 사용
### 1. If 조건문
- 문법
```python
if <expression(참/거짓)>:
    <코드 블럭>
else:
     <코드 블럭>

if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```
- 들여쓰기 tap, 4spaces 
### 1.1 elif

2개 이상의 조건을 활용할 경우
  
```python
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

- 순서에 유의해야됌 (제일 많은걸 거르는 곳에서 다빠져버리는 형태가 될 수 있음)
- 나쁜예
 ```python
 # dust = 100 일경우 보통으로 표시되어버림
if 30 >= dust:
    print('좋음')
elif dust >= 30:
    print('보통')
elif dust >= 80:
    print('나쁨')
elif dust >=150:
    print('매우나쁨')
```

### 1.2 중첩 조건문

조건문은 다른 조건문에 중첩이 가능
```python
## dust 150 초과인 경우 = '매우 나쁨'
# dust 300 초과인 경우 추가적으로 '실외 활동을 자제하세요.'출력,
if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
elif dust > 80:
    print('나쁨')
```

### 1.3 Conditional Expression (조건 표현식)

Ternary Operator(삼항 연산자)라고도 부름

```python
#활용법
true_value if <조건식> else false_value
```

```python
num = 2
if num % 2:
    result = 'Odd number'
else:
    result = 'Even number'
print(result)

=
num = 2
result = 'Odd number' if num % 2 else 'Even number'
print(result)
```

## 2. Loop Statement (반복문)

- While
- For

### 2.1 while 

while 문은 조건식이 참(True)인 경우 반복적으로 코드를 실행

```python
#활용법
while <조건식>:
    <코드 블럭>

while True:
    print('조건식이 참일 때까지')
    print('계속 반복')
```
**주의사항**

1. 반드시 종료조건을 설정해야 합니다.
2. `while` 문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요

```python
# 예시 (안녕이라고 적을때까지 '안녕?' 계속 표시)
user_input = ''

while user_input != '안녕':
    print('안녕?')
    user_input = input() 
```

**`어려웠던 예시`**
```python
# num이 10 일때까지 계속 더한다
num = 10
total = 0

while num > 0:
    total += num    
    num -= 1

print(total)
= 55
```

### 2.2 for
`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회

```python
#활용법
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>

for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
```

```python
#한글자씩 표현할때
chars = input('')

for char in chars:
    print(char)
```
### 2.2.1 딕셔너리 순회(반복문 활용)
* dictionary에서 `for`를 활용하는 4가지 방법

```python
# 0. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])
    
    
# 2. `.values()` 활용
# 이 경우 key는 출력할 수 없음
for val in dict.values():
    print(val)

    
# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)

# .items() 는 튜플들로 이루어져 있음 => 임시변수에서 tuple 할당 가능
for key, val in grades.items():
    print(key, val)

```

### 2.2.2 enumerate()

인덱스(index)와 값(value)을 함께 활용 가능

```python
# 활용법
enumerate(members)
= <enumerate at 0x168525e9400> # 결과는 = 주소 값

list(enumerate(members))
= [(0, '민수'), (1, '영희'), (2, '철수')]

for idx, member in enumerate(members):
    print(idx, member)

0 민수
1 영희
2 철수

#튜플로 값이 나온다 
```

- 숫자를 1부터 카운트 할 수도 있음(100,1000도 가능)
```python
for idx, member in enumerate(members, start = 1):
    print(idx, member)

1 민수
2 영희
3 철수
```

## 3. List Comprehension

여러 줄의 코드를 한 줄로 줄일 수 있음

```python
# 문법
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```
```python
word = 'python'

# for 문 방식
answer = []  
for char in word:
    answer.append(char * 3)
print(answer)  # ['ppp', 'yyy', 'ttt', 'hhh', 'ooo', 'nnn']

# list-comprehension 방식
[char * 3 for char in word]
```

**임시변수에 값을 전혀 사용하지 않는다면, _ 로 쓰자!**

### 3.1 Dictionary comprehension
```python
# 문법
{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})
```

```python
# dict 에 새로운 k-v 추가하기
a = {}
a['key'] = 'value'
print(a)

# 1~3의 세제곱 딕셔너리 만들기
cubic_dict = {}

for i in range(1, 4):
    cubic_dict[i] = i ** 3

print(cubic_dict)  # {1: 1, 2: 8, 3: 27}

cubic_dict = {i: i**3 for i in range(1, 4)}
print(cubic_dict)
```

### 3.2 for 과 if 같이 사용
```python
# 반복 + 조건

# 1~30까지 숫자 중에 홀수만 출력
for num in range(1, 31):
    # 홀수일 경우에만
    if num % 2:
        # 출력
        print(num)
```

### 3.3 break, continue, for-else (반복제어)
### 3.3.1 break 
```python
ex)
# 종료조건 없이 n을 1씩 증가시키는 while 반복문 안에서 
# n이 3이 되는 경우에 break되어 반복문을 종료하는 코드를 작성해봅시다.

n = 0
while True:
    print(n)
    n += 1

    if n == 3:
        break

0
1
2
```

```python
ex)
rice = ['보리', '보리', '보리', '쌀', '보리']

for grain in rice:
    print(grain)
    if grain == '쌀':
        print('잡았다!')
        break

보리
보리
보리
쌀
잡았다!
```

### 3.3.2 continue

뜻 : 건너뛰다, 배제하다
```python
ex)
# for문을 통해 0~5까지의 숫자를 반복하며,짝수인 경우 continue하고,홀수인 경우 해당 숫자를 출력

for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
1
3
5

#한마디로 1부터 6까지 중에 2로나눴을때 나머지가 0 인값을 배제하라
```
```python
ex)
ages = [10, 23, 8, 30, 25, 31]

for age in ages:
    if age < 20:
        continue
    print(age)

23
30
25
31
```

### 3.3.3 pass

아무것도 안함, 들여쓰기 이후 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```
0
1
2
3
4

### 3.3.4 else

끝까지 반복문을 실행한 이후에 실행됩니다.

- 반복문이 break 문으로 종료될 때는 실행 안됌 (즉, break를 통해 중간에 종료되지 않은 경우만 실행)
- **즉, break 가 없는 for 문에서는 사용할 이유가 없음**

```python
ex)
for char in 'banana':
    # 'b' 가 존재하는 경우,
    if char == 'b':
        print('b!!!')
        break 
else:
    print('b가 없습니다.')

= b!!!
```
```python
ex) #만약 break가 없으면 결과에 b가 없습니다가 출력됌
for char in 'banana':
    # 'b' 가 존재하는 경우,
    if char == 'b':
        print('b!!!')
        break 
else:
    print('b가 없습니다.')

= b!!!
b가 없습니다.
```