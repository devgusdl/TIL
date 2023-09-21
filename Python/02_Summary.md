# Container
## type of Container
## 1. Sequence (시퀀스형)
mean : ordered data: not sorted (순서대로 나열된 형식,정렬x)
### 1.1 List (Mutable 가변형)
my_list = [value1, value2, value3]

- How to name a variable
    1. 무슨 데이터가 있는지 유추가 가능한 이름
    2. 복수형 이름으로 짓기(container)
    3. _list 붙이기(선택)

||Object1|Object2|Object3|Object4|
|---|---|---|---|---|
|Positive index|0|1|2|3|
|Negative index|-4|-3|-2|-1|

- Can add other type of data
```python
boxes = ['A', 'B',['apple', 'banana', 'cherry']] 

boxes[-1] 
= ['apple', 'banana', 'cherry']

boxes[2][2]
= 'cherry'

boxes[-1][1][0]
= 'b'
```
- Object 접근,수정,추가,삭제 가능
```python
numbers = [1, 2, 3, 4, 5]

# 접근
numbers[2]

#수정
numbers[2] = 30
print(numbers)

#추가
numbers.append(6) #소괄호 있으면 함수
print(numbers)

# 6 <=> 30 위치 바꾸기
numbers[5], numbers[2] = numbers[2], numbers[5]

#삭제
numbers.pop() #맨뒤에꺼 하나 삭제됌 
print(numbers)
```
### 1.2 Tuple (Immutable 불변형)

About tuple
- 리스트랑 유사하지만, (소괄호)로 묶어서 표현함
- 데이터 추가/수정/삭제 불가능 (접근은 가능)
```python
numbers = (1, 2, 3)
numbers[1] 
= 2
```

- 사용 방법
```python
my_tuple = (2, 4)
print(my_tuple, type(my_tuple))

another_tuple = 2, 4, 10
print(another_tuple)
```
- 주의 사항
```python
#단일 항목의 경우
a = (1)
print(a, type(a))
이렇게 쓰면 int라고 나오기 때문에

a = (1,) 이렇게 써야함
```
```python
#복수 항목의 경우
multi_tuple = (1, 2, 3, )
print(multi_tuple)

= (1, 2, 3)
```
```python
# 아무것도 적지않아도 튜플타입이다
empty = ()
print(empty, type(empty))
=() <class 'tuple'> 
```

### 1.3 Range (Immutable 불변형)

정수의 시퀀스를 나타내기 위해 사용함

- 기본형 
  range(start, end, [step, ])
```python
범위 지정 : range(n, m)

n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : range(n, m, s)

n부터 m-1까지 +s만큼 증가한다
```
- 수정 불가능
- Example
```python
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(9, 0, -2))
[9, 7, 5, 3, 1]
```
### 1.4 String(x)
### 1.5 binary (x)

### 1.6 Packing / Unpacking Operator (패킹/언패킹 연산자)
- 모든 시퀀스형(리스트, 튜플 등)은 패킹/언패킹 연산자 * 를 사용하여 객체의 패킹 또는 언패킹이 가능 (묶고 풀고 이런 개념)

```python
x, *y = i, j, k ...
```
1. Packing

- 대입문의 좌변 변수에 위치합니다.
- 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입합니다.
- 나머지 항목들은 모두 별 기호 표시된 변수에 리스트로 대입합니다.

```python
x, *y = 1, 2, 3, 4, 5
print(x, y)

= 1 [2, 3, 4, 5]
```

2.. Unpacking
- argument 이름이 *로 시작하는 경우, argument unpacking이라고 부릅니다.
- 패킹의 경우, 리스트로 대입합니다.

**Packing / Unpacking 연산자 주의사항**

` * ` 연산자가 곱셈을 의미하는지 패킹/언패킹 연산자인지 구분하여야 합니다.
- Packing / Unpacking Operator
    1. 연산자가 대입식의 좌측에 위치하는 경우
    2. 연산자가 단항 연산자로 사용되는 경우
        - 단항 연산자 : 하나의 항을 대상으로 연산이 이루어지는 연산자
        
        
- 산술연산자의 경우
    1. 연산자가 이항연산자로 사용되는 경우
        - 이항 연산자 : 두 개의 항을 대상으로 연산이 이루어지는 연산자

## 2. Non-Sequence (비 시퀀스형)
### 2.1 Set (Mutable 가변형)
- 순서가 없고 중복된 값이 없는 자료구조(집합이랑 비슷)
- {중괄호}를 통해 만든다
- Object 삽입,변경,삭제 가능
```python
s = {1, 2, 3, 2, 1}

# 추가
s.add(4)
print(s)

#삭제
s.remove(2)
print(s)
```
- 빈 세트는 set()을 사용 ({} 불가능) 
- 차집합(-), 합집합(|), 교집합(&) 활용 가능
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1 - s2
s1 | s2
s1 & s2   #활용가능
```
```python
# set은 중복된 값이 있을 수 없습니다.
s3 = {1, 1, 1, 2, 2, 3}
s3

= {1, 2, 3}
```

- set으로 list의 중복된 값을 제거 가능
```python
locations = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']

list(set(locations))
= ['대전', '서울', '부산', '광주']
```
- But, set으로 변환하는 순간 순서를 보장 x


### 2.2 Dictionary (Mutable 가변형)

Dictionary = key + value
```
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```
About dictionary
- { }를 통해 만들며, dict()로 만들 수 있음
- 순서를 보장 x
- key는 변경 불가능(immutable)한 데이터만 가능 (immutable : string, integer, float, boolean, tuple, range)
- value는 list, dictionary를 포함한 모든 것이 가능
```python
phone_book = {'서울': '02', '경기': '031', '인천': '032', '대전': '042', '광주': '062'}

# key list
phone_book.keys()

# value list
phone_book.values() 

# key + value list
phone_book.items()
```
- 할당식을 통해 key-Value 추가 가능
- 할당식을 통해 Value 수정 가능

```python
# dict key 중복 안됨. (value는 무관)
phone_book = {
    '서울' : '02',
    '부산' : '051',
    '인천' : '032',
    '광주' : '062',
    '대전' : '042',    컨테이너 자료형을 여러줄에 쓸 경우, 반드시 Trailing Comma 적을것!!!
}

# 접근 (Key 없으면 Error)
print(phone_book['서울'])
# print(phone_book['평창'])(없는 단어)

# key가 이미 존재한다면 => 수정
phone_book['서울'] = '022'
print(phone_book)

# key가 존재하지 않는다면 = > ke- value 추가 
phone_book['평창'] = '올림픽'
print(phone_book)
```

- dict key는 immutable(불가변형), value는 상관 없음
1. number(int, float)
2. bool
3. `str`
4. tuple
5. range

## 3. Type conversion, Typecasting (형변환)

||str|list|tuple|range|set|dict|
|---|---|---|---|---|---|---|
|srt||o|o|x|o|x|
|list|o||o|x|o|x|
|tuple|o|o||x|o|x|
|range|o|o|o||o|x|
|set|o|o|o|x||x|
|dict|o|o(key)|o(key)|x|o(key)||

- 특징
1. set 중복요소 제거됨
2. str 앞뒤로 ''만 찍힘

# 정리
## 컨테이너(Container)
<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>

## 4.1 Sqeuence Type Operator (시퀸스형 연산자)

- 시퀸스를 연결 가능
  ```python
  # list 연결
  [1, 2] + ['a']
  = [1, 2, 'a']

  # tuple (뒤에 ,를 붙여줘야 튜플이 된다)
  (1, 2) + ('a',)

  # range에는 사용 x
  ex) range(1) + range(5)
  ```

## 4.2 반복연산자 (*)
- 시퀸스 반복 가능
  ```python
  # list 반복
  [0] * 8
  = [0, 0, 0, 0, 0, 0, 0, 0]

  # tuple 
  (1, 2) * 3
  = (1, 2, 1, 2, 1, 2)

  # range에는 사용 x
  ex) range(1) + range(5)

  # str 반복
  'hi' * 3 
  = 'hihihi'
  ```

## 4.2 Indexing/Slicing
### 4.2.1 Indexting
- 시퀀스의 특징 인덱스 값에 접근 가능 
- But 해당 인덱스가 없는 경우 IndexError가 발생

```python
# list 인덱싱 통해 접근
[1, 2, 3][2]
= 3

# Tuple 인덱싱 통해 접근
(1, 2, 3)[0]
= 1

# Range 인덱싱 통해 접근
list(range(1, 10, 2))[2]
= 5

# 문자열 인덱싱 통해 접근
'abc'[0]
= 'a'
```

### 4.2.1 Slicing
```python
print([1, 2, 3, 4][1:4])
print((1, 2, 3)[:2])
print(range(10)[5:8])
print('abcd'[2:4])
```
```python
phone = '010-1234-5678'

phone[9:]   # 뒷자리
phone[-4:]  # 뒷자리
phone[4:8]  # 중간자리
```

### 4.2.2 Function (함수)

특정 명령을 수행하는 함수 묶음
```python
def multiply(x, y, z):
    return x * y * z

multiply(5, 6, 3)

= 90
```
### 4.3 Module (모듈)
- 함수 / 클래스의 모음 또는 하나의 프로그램을 구성하는 단위

### 4.4 Package (패키지)
- 프로그램과 모듈의 묶음
  - 프로그램 : 실행하기 위한 것
  - 모듈 : 다른 프로그램에서 불러와 사용하기 위한 것

### 4.4 Library (라이브러리)
- 패키지의 모음

