# Python
## 1. Syntax
### 1.1 Indentation

들여쓰기 할 때는 4칸(space) or 1탭(tap)

```python
if True:
    print(True)
else:
    print(False)
``` 
### 1.2 Variable
* 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름
* Object : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

### 1.3 Assignment Operator(할당 연산자)

* 변수는 = 을 통해 할당 된다.
* type(), id()
```python
x = 'Kim Hyun'
type(x)
id(X)
```

### 1.4 variable operation(변수연산)
```python
i = 5
j = 3
s = 'Python'

i + j
i - j
i * j
i / j
print(i)

s * 3
= 'PythonPythonPython'

s = 'Python'
s + ' is fun'
= 'Python is fun'
```

### 1.5 Assignment variables(변수 할당)

```python
x = y = 100
print(x, y)
= 100, 100

x, y = 1, 2
print(x, y)
= 1, 2
```

but 다른 값을 동시에, 세 값을 두값에는 안된다
```python
x, y = 1 
or
x, y = 1, 2, 3
```

### 1.6 Identifiers(식별자)
- 영문 알파벳(대문자와 소문자), 언더스코어(_), 숫자로 구성
- 첫 글자에 숫자 x
- 길이에 제한 x
- 대/소문자(case)를 구별
- 아래의 키워드는 사용 x
  ```
  False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

### 1.7 Input
1.7.1 input([prompt])

```python
name = input('Please write your name')
print(name)
```
input = str

### 1.8 Comment(주석)
- 한 줄 주석은 #
- 여러줄 주석
    1. #사용
    2. """ or '''

`드래그하고 ctrl + / 누르면 전부 주석됌`

ex)
```python
# hello
# python
print('''
hello 
python
''')
```

## 2. Data Type
### 2.1 Boolean Type(불린형)
   
   Ture/ False 검증

```python
bool(0) F
bool([]) F
bool(1) T
bool("") F
```
안에 뭐가 있으면 T, 비어있거나 0이면 F 

### 2.2 Numeric Type(수치형)
   - int (정수, integer)
     - 8진수 : 0o / 2진수 : 0b / 16진수: 0x 로도 표현 가능
   - float (부동소수점, 실수, floating point number)
     - e를 사용할 수도 있습니다. (e와 E 모두 사용 가능) ex) 314e-2
```python
# round() 는 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다릅니다.
# round(값, 소수점자릿수) 
round(x, 2)
ex)
round(3.9549, 2)
= 3.95

round(3.9559, 2)
= 3.96
```
   - complex (복소수, complex number)
     - 각각 실수로 표현되는 실수부와 허수부를 가짐, 복소수는 허수부를 j로 표현
```python
a = 3 + 4j
type(a)
= complex
```
### 2.3 String Type(문자열)

- 모든 문자는 str로 표현
```python
age = input('')
type(age)

= str 
```
- ' or " 로 표현 가능
```python
print('hyun \'hi\'')

= hyun 'hi'
```
```
'he\'s friend'

="he's friend"
```
```python
"'small' big""
"'small' big"
```
### 2.4 None 아무것도 없을 떄


## 3. Escape sequence
  
문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 역슬래시 `\`를 활용하여 이를 구분 

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\ |`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|

```python
print('이 다음은 엔터. \n그리고 탭\t탭')

이 다음은 엔터. 
그리고 탭	탭
```

## 4. f-string
- 중괄호를 써야함 {}
```python
name = '김현'
score = 3.5

print(f'내 이름은 {name}, 성적은 {score}')

내 이름은 김현, 성적은 3.5
```
```python
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi * 2 * 2}')

원주율은 3.14. 반지름이 2 일때 원의 넓이는 12.566368
```