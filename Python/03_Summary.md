# Operators (연산자)
## 1. Arithmetic operators(산술연산자) 

|연산자|내용|
|----|---|
|+|덧셈|
|-|뺄셈|
|\*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지(modulo)|
|\*\*|거듭제곱|

- 나눗셈( / )은 항상 float로 나옴
```python
4 / 2
= 2.0
```
- 나머지( % ) 연산 결과가 0이면 배수
```python
#이런 경우 143은 7의 배수 x
143 & 7
= 3    
```
- 음수, 양수
```python
negative = -10
print(+negative)
print(-negative)

= -10
=  10
```
## 2. Comparison operator(비교연산자)

|연산자|내용|
|----|---|
|`<`|미만|산술연산자
|`<=`|이하|
|`>`|초과|
|`>=`|이상|
|`==`|같음|
|`!=`|같지않음|
|`is`|객체 아이덴티티|
|`is not`|부정된 객체 아이덴티티|
- 대소관계 및 같은 숫자 다른숫자
```python
3 < 1       False
1 != 11     True
```
- Type of 비교연산자
```python
type (3 < 1)
= bool
```
- 문자열의 경우
```python
'hi' == 'hi'   True
```

## 3. logical operator(논리연산자)

|연산자|내용|
|---|---|
|a and b|a와 b 모두 True시만 True, False 하나라도 있으면 False|
|a or b|a 와 b 모두 False시만 False, True 하나라도 있으면 True|
|not a|True -> False, False -> True|
  
- and는 a가 거짓이면 a를 리턴하고, a가 참이면 b를 리턴
- or은 a가 참이면 a를 리턴하고, a가 거짓이면 b를 리턴

### 3.1 Short Circuit Evaluation (단축평가)
- and 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환
- or 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환

```python
# and
# 마지막으로 본 false가 뭔지에 따라 결과가 달라짐
1 and 3.14 and 'asdf' and [] and {} and () and True
= []

ex) 3.14 자리에()를 넣으면 결과는 ()로 출력됌

# or
# 하나라도 True값이 나오면 결과는 true인 값으로 나옴
0 or '' or [] or None or 'a' or 1234 or {1, 2}
= 'a'
```

## 4. Complex operator(복합연산자)

|연산자|내용|
|----|---|논리연산자
|a += b|a = a + b|
|a -= b|a = a - b|
|a \*= b|a = a \* b|
|a /= b|a = a / b|
|a //= b|a = a // b|
|a %= b|a = a % b|
|a \*\*= b|a = a ** b|

```python
num = 0

while num < 5:
    print(num)
    num += 1  # num = num + 1
```

### 4.1 Containment Test

in을 통해 속해있는지 확인 가능
```python
# 구간 가능
'a' in 'apple'
'app' in 'apple'  

# list(시퀀스 전부 가능)
2 in [1, 2, 3, 4] 

# range
3 in range(5)
3.4 in range(5) x #실수는 포함하지 않음

#dict(연산을 key 만 확인, value는 확인하지 않음)
1 in {'a': 1}   False
```

### 4.2 Identity

is 동일한 object 확인 가능
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3]

id(l1), id(l2)

= (2633435481088, 2633457575104) #같지 않음
```
- -5 부터 256 까지의 id는 동일합니다.
```python
x = 2
y = 2
id(x), id(y), x is y

= (2633352347920, 2633352347920, True)
```

## 5. Operator precedence(연산자 우선순위)

0. `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자
    `**`
4. 단항연산자 
    `+`, `-` (음수/양수 부호)
5. 산술연산자
    `*`, `/`, `%` 
6. 산술연산자
    `+`, `-`
7. 비교연산자, `in`, `is`
8. `not`
9. `and` 
10. `or`

```python
# 단항연산자와 산술연산자의 우선순위가 다름
ex)
-2 ** 4   
= -16 

(-2)**4
= 16
```