# Funtion (함수 1)
## 1. 함수의 정의

특정한 기능을 하는 코드의 묶음
### 1.1 왜 사용 하는가?
- 가독성
- 재사용성
- 유지보수
### 1.2 활용법
```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```
### 1.3 함수의 선언과 호출
- 함수의 선언은 def 키워드를 활용합니다.
- 들여쓰기(4spaces)로 함수의 body(코드 블록)를 작성합니다.
  - Docstring은 함수 body 앞에 선택적으로 작성 가능합니다.
- 함수는 매개변수(parameter)를 넘겨줄 수도 있습니다.

- 함수는 동작후에 return을 통해 결과값을 전달합니다.
  - 반드시 하나의 객체를 반환합니다 (return 값이 없으면, None을 반환)
- 함수는 호출은 함수명()으로 합니다.
  - 예) func() / func(val1, val2)
  
`참고자료`  [파이썬 문서](https://docs.python.org/ko/3/library/functions.html)
```python
# 랜덤숫자뽑기 (로또)
import random

random.sample(range(1,46),6)
= [랜덤 수 6개]
```

!! 함수 예시
```python
# 두 수 중 더 큰 수 고르기
ex) max(1, 5)
def my_max(num_a, num_b):
    if num_a > num_b:
        return num_a
    else:
        return num_b
# 다른 방법
def my_max(num_a, num_b):
    return num_a if num_a > num_b else num_b
```
좋은 사이트 추천(데이터 시각화 가능)

[Python tutor](http://pythontutor.com/visualize.html#code=num1%20%3D%200%0Anum2%20%3D%201%0A%0Adef%20func1%28a,%20b%29%3A%0A%20%20%20%20return%20a%20%2B%20b%0A%20%20%20%20%0Adef%20func2%28a,%20b%29%3A%0A%20%20%20%20return%20a%20-%20b%0A%20%20%20%20%0Adef%20func3%28a,%20b%29%3A%0A%20%20%20%20return%20func1%28a,%205%29%20%2B%20func2%285,%20b%29%0A%20%20%20%20%0Aresult%20%3D%20func3%28num1,%20num2%29%0Aprint%28result%29&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
## 2. Output
## 2.1 함수의 return

함수는 반환되는 값이 있으며, 어떠한 종류값이라도 상관없다.
BUT 한개의 객체만 반환된다.
함수가 return되거나 종료되면 함수를 호출한 곳으로 돌아감

### 2.2 practice 1 사각형의 넓이
- [입력 예시] : rectangle(30, 20)
- [출력 예시] : (600, 100)
- 이번 함수는 넓이와 둘레 2가지 값을 한번에 반환하는 함수입니다.
- 넓이 : 너비 * 높이
- 둘레 : 2 * (너비 + 높이)

>def 함수이름(너비, 높이): 넓이와 둘레를 구하고 저장하는 코드를 작성합니다.저장된 넓이, 둘레를 함께 반환합니다.
```python
def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

print(rectangle(30,20))
= (600,100)
```
### 2.3 practice 2 함수 정의, 값 반환
- my_list_max([10, 3], [5, 9])
- 예시 출력) [5, 9]
- 입력되는 리스트a의 요소들의 합을 구하고,입력되는 리스트b의 요소들의 합을 구하고,계산한 두 값을 비교합니다.
> def 함수이름(리스트a, 리스트b):if문을 활용하여 각 리스트 요소의 합을 비교하고 값이 큰 리스트를 반환하는 코드 작성
```python
def my_list_max(list_a, list_b):
    total_a = total_b = 0
    for num in list_a:
        total_a += num
    for num in list_b:
        total_b += num

    if total_a > total_b:
        return list_a
    else:
        return list_b

= def my_list_max(list_a, list_b):
    return list_a if sum(list_a) > sum(list_b) else list_b
```


## 3. Input
## 3.1 매개변수(parameter) & 전달인자(argument)
### 3.1.1 매개변수(parameter)
```python
def func(x):
    return x + 2
```
- x = 매개변수(parameter)
- 입력을 받아 함수 내부에서 활용할 변수
- 정의하는 부분

### 3.1.2 전달인자(argument)
```python
func(2)
```
- 2는 전달인자(argument)
- 실제로 전달되는 값
- 호출하는 부분

### 3.2 함수의 인자

함수는 입력값(input)으로 인자(argument)를 넘겨줄 수 있다

**위치인자(Positional Arguments)**
: 기본적으로 인자는 위치에 따라 함수내에 전달

### 3.2.1 practice 3 원기둥의 부피
- 원기둥 부피 : 원의 넓이 * 높이, 3.14 * 반지름 * 반지름 * 높이
- 3.14 * (반지름의 제곱) * 높이
- 3.14 * 반지름 * 반지름 * 높이
>def 함수이름(반지름, 높이): 원기둥 부피를 계산하여 반환합니다.

```python
def cylinder(r, h):
    answer = 3.14 * r**2 * h
    return round(answer, 3)
    # return 3.14 * r**2 * h

print(cylinder(5, 2))
print(cylinder(2, 5)) # 순서를 바꾸면 다른 값이 나온다
= 157 , 62.8
```
### 3.3 기본 인자 값(Default Argument Values)
함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않도록하여, 정의된 것 보다 더 적은 개수의 인자들로 호출 될 수 있습니다.
```python
# 활용법
def func(p1=v1):
    return p1
```
### 3.3.1 practice 4 기본 인자 값 활용
**입력된 값이 없을 때** 라는 상황과 **그 상황에서 사용할 값**이라는 점에 주의합니다.

- 입력된 값이 길동 => '길동, 안녕?'
- 값이 없는 경우 => '익명, 안녕?'

```python
def 함수이름(이름='입력이 없으면 사용할 값'):
    # 매개변수를 활용하여 문장(문자열)을 완성하여 리턴
```
```python
def greeting(name='익명'): # 여기에 ='익명'을 적지 않으면 작동 안함
    return f'{name}, 안녕'

print(greeting('철수'))
print(greeting())
= 철수, 안녕
익명, 안녕
```
**\*주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.**
```python
# 이렇게 앞에는 = 는 '뭐뭐'를 썼는데 뒤에 age에는 =''가없으면 안된다. 하나만 쓰고 싶으면 age에 쓰던가 자리를 바꿔야함!!!
def greeting(name='john', age):
    return f'{name}은 {age}살입니다.'

greeting(20)
```
>def 함수이름(기본인자가 아닌 친구들, 기본인자):
    매개변수를 활용하여 문장(문자열)을 완성해서 반환합니다.

### 3.4 키워드 인자(keyword arguments)
**함수를 호출할 때** 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.
```python
def greeting(age, name, address, major):
    return f'{name}은 {age}살입니다. 전공은 {major}, 주소는 {address}입니다.'
```
!!이렇게 썼을 때 name, age, major, address의 순서를 바꿔쓰면 오류가 난다

만약 쓰고싶으면 
```python
greeting(name='김현', major='행관', age=20, address='서울')
```

### 3.5 가변(임의) 인자 리스트(Arbitrary Argument Lists)
앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 **함수를 정의할 때** 가변 인자 리스트`*args`를 활용

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현 

---

**활용법**

```python
def func(a, b, *args):
```
> `*args` : 임의의 개수의 위치인자를 받음을 의미
> 
> 보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 옵니다.

```python
ex)
def func(*args):
    print(args, type(args))

func(10, 20, 30, 40, True, 'asdf')
```

### 3.5.1 practice 5 가변 인자 리스트 사용
용어 이름은 가변 인자 리스트이지만, 기본적으로 튜플 자료형임에 주의합니다.
- `*` (별표 1개)를 매개변수에 작성해야합니다.
- 말 그대로 정해지지 않았기 때문에, 이번 예제에서는 반복문을 통해 간편하게 개별 값에 접근합니다.


>def 함수이름(가변 인자 리스트):
    가변 인자 리스트 중 처음 값을 기준이 되는 값으로 할당합니다.
    반복문을 통해 입력 받은 값들을 검사합니다.
    조건문으로 기준이 되는 값과 다른 요소들을 비교해서, 더 큰 값을 기준값으로 변경합니다.
    찾아낸 최대값을 반환합니다.     
```python
# 함수화
def my_max(*args):
    max_val = args[0]
    for num in args:
        if num > max_val:
            max_val = num
    return max_val

print(my_max(3, 1, 2, 4))
= 4
```

### 3.6 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 함수를 정의할 때 가변 키워드 인자 **kwargs를 활용

가변 키워드 인자는 dict 형태로 처리가 되며, 매개변수에 **로 표현합니다.
---

**활용법**

```python
def func(**kwargs):
```
> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미합니다

```python
ex)
def my_func(a, b=1, *args, **kwargs):
    print(a, b, args, kwargs)
    
my_func(1, 2, True, False, 'a', x=1, y=2, z=3)
= 1 2 (True, False, 'a') {'x': 1, 'y': 2, 'z': 3}
ex)
def my_dict(**kwargs):
    return kwargs

print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
```

# Funtion (함수 2)
## 1. 함수와 스코프(scope)
### 1.1 스코프 종류
- 전역 스코프`(global scope)`: 코드 어디에서든 참조할 수 있는 공간
- 지역 스코프`(local scope)`: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
- 전역 변수`(global variable)`: 전역 스코프에 정의된 변수
- 지역 변수`(local variable)`: 로컬 스코프에 정의된 변수
```python
a = 10  # a => global
        # b, c => local
def func(b):
    c = 20
    print(a, b, c)
func(a)
```

**특징**
1. 함수 밖의 변수(global var), 함수 안의 변수(local var)
- 인자는 함수 안의 변수 취급한다.
2. 함수 안(local scope)에서는 함수 밖(global scope)에 접근 가능하다.
- 함수 안에 `a`가 없으면, 함수 밖에서 `a`를 찾는다.
- 만약, 함수 안에 `a`가 있다면, 함수 밖 `a`는 접근할 수 없다.
3. 함수 밖에서는 함수 안에 접근이 불가능하다.

### 1.2 변수의 수명주기(lifecycle)
변수의 이름은 각자의 `수명주기(lifecycle)`가 있음
* **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지
* **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지
* **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)

### 1.3 이름 검색(resolution) 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

아래와 같은 순서로 이름을 찾아나가며, `LEGB Rule` 이라고 부름
* `L`ocal scope: 함수
* `E`nclosed scope: 특정 함수의 상위 함수 
* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

|이름공간|    |    |    |값공간 |    |    |    |    |    |    |
|---|---|---|---|---|---|---|---|---|---|---|
|*Built-ins*|   |   |   |   |   |   |   |   |   |***-5*** |
|   |\|*Global*|   |   | \|  |   |   |   |   |   |***-4***|
|print|\| |`\|`*Local* |`\|`  | \| |  |   |   |   |   |***-3***|
|max|\|   | `\|`  | `\|`  |  \|  |   |   |   |   |   |***...***   |
|min|\|   |  `\|` |  `\|` |  \|  |   |   |   |   |   |***7***|
|sum|\|   |  `\|` |  `\|` |  \|  |   |   |   |   |   |***8***   |
|int|\|   |  `\|` |  `\|` |  \|  |   |   |   |   |   |***9***   |
|str|\|   |  `\|` |  `\|` |   \| |   |   |   |   |   |***...***   |
|dict|\|   | `\|`  | `\|`  |  \| |   |   |   |   |   |***255***   |
|range| \|  | `\|`  |  `\|` |  \| |   |   |   |   |   |***256***   |

```python
ex)
print = 'bibibig'

# print(123)  실행 불가

del print

print(123)


# 1. `print()` 코드가 실행되면
# 2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
# 3. `print`라는 식별자를 Global scope에서 찾아서 `print = 'bibig'`를 가져오고, 
# 4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됌
# 5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문
```
```python
ex) 스코프 설명
a = 10  # Global
b = 20  # Global

def enc():
    print('부모함수')  # Built-ins
    a = 100  # Local (enc)
    print(a)

    def loc():
        c = 40  # Local (loc)
        print(a)  # Enclosed (enc)
        print(b)  # Global
        print(c)  # Local (loc)

    loc()

enc()
```
### 1.3.1 전역 변수 변경 
**`not work`**
```python
global_num = 1
def local_scope():
    global_num = 100
    print('local', global_num)

local_scope()

print('global', global_num)

= local 100
global 1
#결과는 바뀌지 않음 
```
**`How to change`**
```python
num = 1
def local_scope():
    global num
    
    num = 100
    print('local?', num)

local_scope()

print('global', num)

= local? 100
global 100
```
### 1.3.2 
* 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
* 해당 스코프에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
    * 변수에 접근은 가능하지만, 해당 변수를 재할당할 수는 없음
    * 값을 할당하는 경우 해당 스코프의 이름공간에 새롭게 생성되기 때문
    * **단, 함수 내에서 필요한 상위 스코프 변수는 인자로 넘겨서 활용** (클로저 제외)
* 상위 스코프에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
    * 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생

   ## 2. 재귀함수(recursive function)

   재귀함수: 함수 내부에서 자기 자신을 호출하는 함수

   알고리즘을 설계 및 구현에서 유용하게 활용됌
   ### 2.1 팩토리얼 계산
 $$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$
---
Case(1) = `1! = 1`

Case(2) = `2! = 1 * 2` = Case(1) * 2

Case(3) = `3! = 1 * 2 * 3` = Case(2) * 3

...
Case(N) = N! = 1 * 2 * 3 * ... * N = Case(N-1) * N => N-1 단계까지의 결과 * N

```python
def 팩토리얼재귀(현재 단계의 숫자):
    만약, 현재 단계가 1 단계라면?
        더이상 재귀호출을 진행하지않고, 1을 반환
    그렇지 않은 경우에는 (현재 단계의 숫자 * 이전 단계의 재귀 함수의 실행 결과)를 반환
# 예제
def factorial(n):
    # **Base Case**
    if n == 1:
        return 1

    return n * factorial(n-1)

factorial(5)
= 120
```
### 2.2 반복문을 이용한 팩토리얼 계산

반복문으로 구현
- 목표하는 n값 만큼 반복하여 곱을 누적
 
 
```python
def 팩토리얼반복(현재 단계의 숫자):
    시작하는 숫자는 1
    while문을 활용하여, n번만큼 결과에 곱을 누적
    최종 결과를 리턴
# 예제
def fact_while(n):
    total = 1

    while n > 1:
        total *= n
        n -= 1

    return total
```
### 2.3 반복문과 재귀함수

```python
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

* 두 코드 모두 원리는 같습니다.


### 2.3.1 반복문 코드
- n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소
- 마지막에 n이 1이면 더 이상 반복문을 돌지 않음
  
  
### 2.3.2  `재귀 함수 코드`
- 재귀 함수를 호출하며, n은 1씩 감소
- 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않음
* 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 됌

* 재귀함수를 작성시에는 반드시, `base case`가 존재 해야됌 

* `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳을 의미 

* 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1일때, 함수가 아닌 정수 반환하는 것**
* 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용
* 코드가 더 직관적이고 이해하기 쉬운 경우가 있음
* 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있음
* 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생깁니다.
* 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료됌 (최대 재귀 깊이)

### 2.3.3 최대 재귀 깊이
### 최대 재귀 깊이


```python
def recursive():
    print('Hello, recursive!')
    recursive()
 
recursive()
```
---

`recursive()`를 호출하면 아래와 같이 문자열이 계속 출력되다가 RecursionError가 발생합니다.

파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있기 때문입니다.

주피터 노트북은 커널이 종료되어 확인하기 어렵습니다.

---

```bash
Hello, world!
Hello, world!
...
Hello, world!
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)

...

      1 def hello():
      2     print('Hello, world!')
----> 3     hello()
      4 
      5 hello()

RecursionError: maximum recursion depth exceeded while calling a Python object
```
### 2.4 피보나치 수열

첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열 

(0), 1, 1, 2, 3, 5, 8

$$
\displaystyle F_0 = 0
$$


$$
\displaystyle F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$
```python
Case(0) = 0

Case(1) = 1

Case(2) = Case(1) + Case(0) = 1

Case(3) = Case(2) + Case(1)

...

Case(N) = Case(N-1) + Case(N-2)
```
1) `fib(n)` : 재귀함수
```python
def 피보나치재귀(현재단계):
    만약, 현재단계가 2단계보다 작으면
        그냥 현재 단계를 반환
    그렇지 않다면,
        전단계의 재귀함수 + 전전단계의 재귀함수 의 결과를 반환

# 예제 
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

fib(7)
= 13
```
2) `fib_loop(n)` : 반복문 활용한 함수
```python
def 피보나치반복(현재단계):
    만약, 입력된 단계가 2보다 작다면
        입력된 단계를 그대로 리턴!

    결과를 저장할 기본 리스트([0, 1])를 준비 (각각 Case(0)와 Case(1)의 결과)
    반복문을 시작(2부터 시작, N까지)
        마지막 2개의 요소들의 합을 리스트에 추가

    리스트의 마지막 값을 반환

# 예제
def fib_loop(n):
    # 기존 작업물을 저장해둠
    result = [0, 1]

    for _ in range(n-1):
        result.append(result[-1] + result[-2])

    print(result)
    return result[-1]

fib_loop(10)
= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
55

``` 

2-1 ) `fib_loop(n)` : 반복문 활용한 함수
(not list)

- 반드시 리스트로 모든 값을 저장할 필요가 있을까요?
- 실제로 매 반복문 마다 필요한 값은 (마지막 2개의 요소)였습니다.
- 그렇기 때문에 변수 2개에 값을 변경 & 덮어쓰기 하면서 로직을 구성할 수 있음!

```python
def 피보나치반복(현재단계):
    만약, 입력된 단계가 2보다 작다면
        입력된 단계를 그대로 리턴!

    결과를 저장할 변수를 2개 준비 (각각 Case(0)단계와 Case(1)단계의 결과를 의미)
    반복문을 시작(0부터 N-2까지)
        전 단계의 값과 전전 단계의 값의 합을 전 단계에 덮어쓰기하면서, 동시에 원래가지고 있던 전 단계 값을 전전 단계에 저장

    마지막 결과 값을 반환!

# 예제
def fib_loop(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b

    return b
fib_loop(10)
= 55
```

### 2.5 반복문과 재귀함수의 차이

* 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용
* 재귀 호출은 `변수 사용` 을 줄여줄 수 있음
```python
# 재귀호출(재귀 호출은 입력 값이 커질 수록 연산 속도가 오래걸림)
from datetime import datetime

start = datetime.now()
fib(39)
end = datetime.now()

print(end-start)
= 0:00:16.249032

# 반복문 (반복문은 재귀로 구현된 함수보다 연산 속도가 빠른 편)
start = datetime.now()
fib_loop(50000*2)
end = datetime.now()

print(end-start)
= 0:00:00.119999
```

---
## 3. 함수 응용
### 3.1 map(function, iterable)

* 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려줌
* return은 `map_object` 형태
```python
ex) 모든 단어들의 모음을 삭제하려면?
# 일반 식
a = ['1', '2', '3']

b = []

for x in a:
    b.append(int(x))

# [1, 2, 3]
b
```
```python
ex) # map 활용 식
list(map(int, ['1', '2', '3']))
```
**`예시`**
```python
# 1 세제곱의 결과를 나타내는 함수
def cube(n):
    return n ** 3

# 2 세제곱 함수를 각각의 요소에 적용한 결과값
numbers = [1, 2, 3]

# 3 list comprehension
[cube(num) for num in numbers]

# 4 map 활용
list(map(cube, numbers))
```



### 3.2 filter(function, iterable)
* iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환
* `filter object` 를 반환
```python
# 홀수를 판별하는 함수가 있습니다.
def is_odd(number):
    if number % 2:
        return True
    else:
        return False

def is_odd(number):
    return number % 2

list(map(is_odd, numbers))     # [F, T, F, T, F, ...]
list(filter(is_odd, numbers))  # [1, 3, 5, 7, 9]
```


### 3.3 lambda 함수
* 표현식을 계산한 결과 값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림

* return 문을 가질 수 없고, 간단한 조건문 외의 구성이 어려움

* 함수를 정의해서 사용하는 것보다 간결하게 사용 가능

```python
def triangle_area(b, h):
    return 0.5 * b * h

lambda b, h: 0.5 * b * h
```
```python
# 이름있는 변수 => 기명
i = 10
l = [1, 2, 3]
r = range(5)

# 이름없는 변수 => 익명
10
[1, 2, 3]
range(5)
```
**`Change to lambda`**
1. def 를 지우고 lambda 라고 적는다.
2. 함수 이름과 소괄호를 지운다.
3. : 뒤에 엔터와 return 키워드를 지운다.
```python
# 기명함수
def f1(x, y):
    return x + y

print(f1(1, 2))

# 익명함수
f2 = lambda x, y: x + y

print(f2(3, 4))

(lambda x, y: x + y)(1, 3)
```