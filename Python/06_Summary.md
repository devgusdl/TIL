# 데이터 구조(Data Structure)
<데이터의 분류>
- 순서가 있는 데이터(시퀀스)
  - 리스트
  - 튜플
  - 문자열
- 순서가 없는 데이터(비시퀀스)
  - 셋(set)
  - 딕셔너리(dictionary)

## 순서가 있는 데이터 구조
### 문자열(string)

변경할 수 없고, 순서가 있고, 순회가능한
### 1. 조회/ 탐색
### 1.1.find(x)
x의 **첫 번째 위치**를 반환합니다. 만일 문자열내에 x가 없으면, `-1`을 반환합니다.
```python
a = 'apple'
a.find('p') 
= 1 # 제일 첫번째 p자리가 나옴

# 문자가 없을때
a.find('z')
= -1
```
### 1.2 .index(x)
x의 **첫 번째 위치**를 반환합니다. 만일 x가 리스트 내에 없으면, 오류가 발생합니다.
```python
a = 'apple'
a.index('p')
= 1
# 없을때
a.index('z')
= 에러 발생
```
### 1.3 .starswith(x) / .endswith(x)
- `.startswith(x)` : 문자열이 x로 시작하면 True를 반환하고 아니면 False를 반환합니다.
- `.endswith(x)` : 문자열이 x로 끝나면 True를 반환하고 아니면 False를 반환합니다.
```python
a = 'hello python!'
a.startswith('hello')
= True
```

### 1.4 is~ 
- 문자열 검증 메서드
1. `.isalpha()` : 문자열이 (숫자가 아닌)글자로 이루어져 있는가?
2. `.isspace()` : 문자열이 공백으로 이루어져 있는가?
3. `.isupper()` : 문자열이 대문자로 이루어져 있는가?
4. `.istitle()` : 문자열이 타이틀 형식으로 이루어져 있는가?
5. `.islower()` : 문자열이 소문자로 이루어져 있는가?
- 숫자 판별 메서드
1.  `.isdecimal()`: 문자열이 0~9까지의 수로 이루어져 있는가?
2.  `.isdigit()`: 문자열이 숫자로 이루어져 있는가?
3.  `.isnumeric()`: 문자열을 수로 볼 수 있는가?
```python
a = '    n'
b = '\n \t '

a.isspace()
b.isspace()
= True
```

### 2.문자열 변경
### 2.1 .replace(old, new[, count])
- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.
- count를 지정하면 해당 갯수만큼만 시행합니다.
```python
예시 1)
a = 'yaya!'
b = 'wooooowoo'

print(a.replace('y', 'h'))
print(a)

=haha!
yaya!

예시 2)
b.replace('o', '_', 2)
= 'w__oowoo'
```

### 2.2 .strip([chars])
- 특정한 문자들을 지정하면, 양쪽을 제거하거나(`strip`) 왼쪽을 제거하거나(`lstrip`), 오른쪽을 제거합니다(`rstrip`).
- `chars` 파라미터를 지정하지 않으면 공백을 제거합니다.
```python
a = '   hello!  \n'
b = 'hihihihahahahihi'
c = 'monty python'

# strip 양쪽공백
a.strip()
= 'hello!'

# lstrip 왼쪽 공백
a.lstrip()
= 'hello!  \n'

# rstrip 오른쪽에서부터 글자 hi를 제거
b.rstrip('hi')
= 'hihihihahaha'

# `chars` 파라미터를 지정한 경우,rstrip 으로 ' python'을 제거
c.rstrip(' python')
= 'm' python알파벳이 다 지워짐
```

### 2.3 .split([chars])
문자열을 특정한 단위로 나누어 리스트로 반환
```python
# _를 기준으로 문자열 나누기
a = 'a_b_c'
a.split('_')
= ['a', 'b', 'c']

# 모두 붙어있는 문자열을 리스트로 만드려면? 
# '1234'.split('')  # => Nope
list('1234')

= ['1', '2', '3', '4']
```

### 2.4 separator'.join(iterable)
iterable 의 문자열들을 separator(구분자)로 이어 붙인(`join()`) 문자열을 반환

다른 메서드들과 달리, <u>**구분자**</u>가 join 메서드를 제공하는 문자열
```python
word = '배고파'
words = ['안녕', 'hello']

# 문자열 사이에 !넣기
'!'.join(word)
= '배!고!파'

# 문자 합치기
''.join(words)
= '안녕hello'

# 다 붙어있는 문자열을 리스트로 바꾸려면 list()
list('1234')
= ['1', '2', '3', '4']
```
### 2.5 .capitalize(), .title(), .upper()
* `.capitalize()` : 앞글자를 대문자로 만들어 반환
* `.title()` : 어포스트로피(*'*)나 공백 이후를 대문자로 만들어 반환
* `.upper()` : 모두 대문자로 만들어 반환
* 원본 데이터 출력시 그대로
```python
a = 'hI! Everyone, I\'m kim'

# 앞글자 대문자
a.capitalize()
= "Hi! everyone, i'm kim"

# 각각의 단어 앞글자를 대문자
a.title()
= "Hi! Everyone, I'M Kim"

# 모두 대문자
a.upper()
= "HI! EVERYONE, I'M KIM"
```
### 2.6 .lower(), .swapcase()
* `lower()` : 모두 소문자로 만들어 반환
* `swapcase()` : 대 <-> 소문자로 변경하여 반환
* 원본 데이터 출력시 그대로
```python
a = 'hI! Everyone, I\'m kim'

# 모두 소문자
a.lower()
= "hi! everyone, i'm kim"

# 대소문자 변경(대-> 소, 소-> 대)
a.swapcase()
"Hi! eVERYONE, i'M KIM"
```
### 2.7 문자열 메서드 모두 확인 방법
> 파이썬 내장함수 dir을 통해 컨테이너가 가지고 있는 메서드를 확인할 수 있습니다.
> 
> dir('')
---

### 리스트 list
### 3 값 추가 및 삭제 => 원본 변경
### 3.1 .append(x)
- 리스트에 값을 추가할 수 있음
- a[len(a):] = [x] 와 동일
```python 
cafe = ['starbucks', 'tomntoms', 'hollys']
cafe.append('bana')
cafe
= ['starbucks', 'tomntoms', 'hollys', 'bana']
```
### 3.2 .extend(iterable)
- 리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있음
- a[len(a):] = iterable 와 동일
```python
cafe.extend(['wcafe', '빽다방'])
cafe
= ['starbucks', 'tomntoms', 'hollys', 'bana', 'wcafe', '빽다방']

# same
cafe += ['mc_cafe', 'droptop']

# append, extend 차이 
append = 추가하려는 요소를 리스트의 끝에 추가 
ex) [... 'droptop',
 ['coffeenie']]

extend = 다른 리스트의 모든 요소를 현재 리스트에 덧붙임
```
### 3.3 .insert(i, x)
정해진 위치 i에 값을 추가
```python
사용법: list_name.insert(i, x)
# list_name: 요소를 삽입할 대상 리스트의 이름
# i: 삽입할 위치를 나타내는 인덱스 값
# x: 삽입하려는 요소

my_list = [1, 2, 3, 4, 5]

# 리스트의 인덱스 2 위치에 요소 6을 삽입
my_list.insert(2, 6)

print(my_list)

= [1, 2, 6, 3, 4, 5]

```
### 3.4 .remove(x)
- 리스트에서 값이 x인 첫번째 항목을 삭제
- 만일 그런 항목이 없으면 ValueError가 발생
```python
numbers = [1, 2, 3, 1, 2]

numbers.remove(1)
numbers
= [2, 3, 1, 2]
```
### 3.5 .pop([i]) => 삭제되는 값을 return
- 정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환
- i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줌
```python
numbers = [1, 2, 3, 4, 5, 6]
# 가장 앞에 있는 숫자 삭제
print(numbers.pop(0))
= 1
[2, 3, 4, 5, 6]

# 마지막 수 삭제
numbers.pop()
= 6
numbers 
= [2, 3, 4, 5]
```
### 3.6 .clear()
리스트의 모든 항목을 삭제
```python
numbers = [1, 2, 3, 4, 5, 6]
numbers.clear()
numbers
= []
```
### 4 탐색 및 정렬
### 4.1 .index(x)
- x 값을 찾아 해당 index 값을 반환 
- **`앞에와 동일`**
### 4.2 .count(x)
- 원하는 값의 개수를 반환
- **`앞에와 동일`**
```python
a = [1, 2, 5, 1, 5, 1]
a.count(1)
= 3
```
### 4.3 .sort()
- 리스트를 정렬
- 내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, **`None`**을 리턴
- 파라미터로는 `key`와 `reverse`가 있음
```python
# 로또번호 지정하는 코드
import random

lotto = list(range(1, 45))
lucky = random.sample(lotto, 6)

# 정렬을 한다면?
lucky.sort()  # return None
lucky
= [랜덤 정렬된 6자리]

# sort 메서드의 reverse옵션을 이용하면 역순 정렬
lucky.sort(reverse=True)
lucky
= [반대로 정렬]
```

### 4.4 .reverse()
- 리스트의 element들을 제자리에서 반대로 뒤집음
- 정렬하는 것이 아닌 원본 순서를 뒤집고 수정
- 내장함수 `reversed()` 와는 다르게 **원본 list를 변형**시키고, **`None`**을 리턴
- sort와 마찬가지로, 파라미터 `key`와 `reverse`가 있음
```python
classroom = ['Tom', 'David', 'Justin']
print(classroom)

classroom.reverse()
classroom
= ['Justin', 'David', 'Tom'] # 반대로 출력됌
```
### 4.5 리스트 메서드 모두 확인하기
> 파이썬 내장함수 dir을 통해 컨테이너가 가지고 있는 메서드를 확인할 수 있음
>
> help([ ]) # dir([ ])
### 튜플 tuple
- 변경할 수 없는 불변(Immutable) 자료형, 값을 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원
### 5 탐색
### 5.1 .index(x[, start[, end]])
- 튜플에 있는 항목 중 값이 x 와 같은 첫 번째 인덱스를 돌려줍니다.

해당하는 값이 없으면, ValueError를 발생합니다.
### 5.2 .count(x)
튜플에서 x 가 등장하는 횟수
```python
a.count('python')
```
## 순서가 없는 데이터 구조
- 알고리즘에 빈번히 활용되는 순서가 없는(unordered) 데이터 구조
    - 셋(Set)
    - 딕셔너리(Dictionary)
### 셋 set
변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
### 6 추가 및 삭제
### 6.1 .add(elem)
elem을 셋(set)에 추가
```python
a = {'사과', '바나나', '수박'}
a.add('포도')
a.add('포도') # 두번을 추가해도 set 특성에 따라 한번으로 표시
a
= {'바나나', '사과', '수박', '포도'}
```
### 6.2 .update(*others)
- 여러 값을 추가함
- 반드시 iterable 데이터 구조를 전달해야함
```python
a = {'사과', '바나나', '수박'}
a.update({'토마토', '토마토', '딸기'}, {'포도', '레몬'})
a
= {'딸기', '레몬', '바나나', '사과', '수박', '토마토', '포도'}
```
### 6.3 .remove(elem)
- elem을 셋(set)에서 삭제하고, 셋(set) 내에 elem이 존재하지 않으면 KeyError가 발생
```python
a = {'사과', '바나나', '수박'}
a.remove('사과') 
a.remove('apple') # 없는 변수 출력시 오류
```
### 6.4 .discard(elem)
- elem을 셋(set)에서 삭제함
- remove와 다른 점은 elem이 셋(set) 내에 존재하지 않아도, 에러가 발생하지 않음
```python
a = {'사과', '바나나', '수박'}
a.discard('포도')
a.discard('수박')
a
= {'바나나', '사과'}
```
### 6.5 셋(set) 메서드 모두 확인하기
> 파이썬 내장함수 dir을 통해 컨테이너가 가지고 있는 메서드를 확인할 수 있습니다.
> 
> dir(set)
### 딕셔너리(Dictionary)
- 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
- `Key: Value` 페어(pair)의 자료구조
### 7 조회
### 7.1 .get(key[, default])
- key를 통해 value를 가져옴
- key가 존재하지 않을 경우 None을 반환, KeyError가 발생하지 않음
```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
# 없는 key -> dict에 실행
my_dict['pineapple']
= 에러뜸

# 없는 key -> get 메서드로 실행시
my_dict.get('pineapple')
= 에러 안뜸

# key가 없으면 0을 반환하도록 실행
my_dict.get('pine', 0)
= 0
```
### 7.2 .setdefault(key[, default])
- dict.get() 메서드와 비슷한 동작을 하는 메서드로, key가 딕셔너리에 있으면 value를 돌려줌
- get과 다른 점은 key가 딕셔너리에 없을 경우, default 값을 갖는 key 를 삽입한 후 default 를 반환한다는 점
-  만일 default가 주어지지 않을 경우, None 을 돌려줌
```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

my_dict.setdefault('apple')
= '사과'

# setdefault 메서드를 통해 딕셔너리 my_dict의 key 'pineapple'의 value를 가져와서 출력해봅시다.
# 만일 pineapple이 없을 경우, '파인애플'을 출력하도록 함
my_dict.setdefault('pineapple', '파인애플')  # key 있으면 value 반환 / 없으면 두번째 값으로 추가
= '파인애플'

print(my_dict) 출력시 파인애플도 추가해서 나옴
= {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'pineapple': '파인애플'}
```
### 8 추가 및 삭제
### 8.1 .pop(key[, default])
- key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환
- default가 없는 상태에서 해당 key가 딕셔너리에 경우, KeyError가 발생

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

my_dict.pop('apple') # 애플제거 
= 사과 #제거대상
my_dict
= {'banana': '바나나'}

# 없는거 실행시 에러 발생하는데 pop 메서드의 두번째 인자로 default 값을 설정 해 KeyError가 발생하지 않도록 할 수 있음
my_dict.pop('pear', '없다..') # 뒤에 설정
= '없다..'
```
### 8.2 .update([other])
- other 가 제공하는 key,value 쌍으로 딕셔너리를 덮어씁니다. other 는 다른 딕셔너리나 key/value 쌍으로 되어있는 모든 iterable을 사용 가능합니다.
```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}

my_dict.update({'apple': '아이폰'})
my_dict
= {'apple': '아이폰', 'banana': '바나나', 'melon': '멜론'} # 사과 -> 아이폰으로 업데이트됌

# 덮어씌우기, 새로추가
my_dict.update({'mango': '망고'})
= {'apple': '아이폰',
 'banana': '바나나',
 'melon': '멜론',
 'mango': '망고'}
```
### 8.3 딕셔너리 메서드 모두 확인하기
> 파이썬 내장함수 dir을 통해 컨테이너가 가지고 있는 메서드를 확인할 수 있음
>
> dir(dict)
# 얕은 복사와 깊은 복사
### 9 데이터 분류
데이터의 분류에 따라 복사가 달라집니다. 데이터는 크게 변경 가능한 것(mutable)들과 변경 불가능한 것(immutable)으로 나뉨

### 9.1 변경 불가능한(immutable) 데이터
* 리터럴(literal)

    - 숫자(Number)
    - 글자(String)
    - 참/거짓(Bool)

* `range()`

* `tuple()`

* `frozenset()`
```python
# 복사 방법
a = 20
b = a
print(a)
print(b)
= 20
20
```
### 9.2 변경 가능한(mutable) 데이터
- `list`
- `dict`
- `set`

**복사 방법**

파이썬에서 데이터를 복사하는 방법은 크게, 세 가지로 나뉩니다.
> - 할당 (Assignment)
> - 얕은 복사 (Shallow copy)
> - 깊은 복사 (Deep copy)

### 9.3 할당 (Assignment)
```python
# o 값을 지정함
# c 에 o 값을 저장
# c의 값을 바꾸면 o값도 바뀜
# id도 같음 
original = [1, 2, 3]
copy = original

copy[0] = 5
print(copy, original)
= [5, 2, 3] [5, 2, 3]

id(copy), id(original
= (2309212396480, 2309212396480)
#즉, 두개의 중 하나만 변경되어도 나머지 하나도 동일하게 수정되는 현상이 발생하게 됩니다.
```
### 10 얕은 복사(Shallow copy)
### 10.1 slice 연산자 사용 [:]
```python
a = [1, 2, 3]
# slice 연산자로 a의 모든 요소를 b에 저장
# 리스트 b의 첫 번째 값을 5로 바꾸고 a를 출력
# slice 연산자를 활용하면 새로운 리스트 저장가능
b = a[:]
id(a), id(b)
= (2843376385536, 2843376381504) # 값이 다름

a[0] = 5
a, b

= ([5, 2, 3], [1, 2, 3])
```
### 10.2 list() 활용
```python
a = [1, 2, 3]

# list 함수로 리스트 a를 복사하여 b에 저장합니다.
# 리스트 b의 첫 번째 값을 5로 바꾸고 리스트 a를 출력합니다.

b = list(a)
a[0] = 5
a, b

= ([5, 2, 3], [1, 2, 3])
```
### 10.3 .copy() 활용
```python
a = [1, 2, 3]
b = a.copy()
a[0] = 10
a, b

= ([10, 2, 3], [1, 2, 3])
```
### 11 깊은 복사(Deep copy)
* 만일 중첩된 상황에서 복사를 하고 싶다면, `깊은 복사(deep copy)`를 해야함
* 깊은 복사는 새로운 객체를 만들고 원본 객체 내에 있는 객체에 대한 복사를 재귀적으로 삽입
* 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경됌
```python
# 내부에 있는 리스트까지 복사를 하기 위해서 copy 모듈을 활용합니다.
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
a, b

= ([1, 2, [1, 2]], [1, 2, [1, 2]])
```