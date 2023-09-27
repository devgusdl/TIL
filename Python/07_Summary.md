# OOP

- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)
- 클래스(Class)와 객체(Object)

## 1. Object(객체)
- Python에서 **모든 것은 객체(object)** 이다
- 모든 객체는 **타입(type), 속성(attribute), 조작법(method)** 을 가진다

객체(Object)의 특징

- **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가? 
- **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
- **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

# 객체 지향 프로그래밍(Object-Oriented Programming)

Object가 중심(oriented)이 되는 프로그래밍

**<wikipedia - 객체지향 프로그래밍>**
>
> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나
>
> 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임 + 상호작용(메서드)으로 파악하고자 하는 것

## 절차 중심 vs. 객체 중심

> 프로그래밍 패러다임: 어떻게 프로그램을 작성할 것인가


## 객체 중심의 장점


**<wikipedia - 객체지향 프로그래밍>**
> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용 
>
> 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있음

- 코드의 **직관성**

- 활용의 **용이성**

- 변경의 **유연성**

## OOP 기초

### 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

# 인스턴스(instance) 생성
my_instance = MyClass()

# 속성 접근
my_instance.my_attribute

# 메서드 호출
my_instance.my_method()
```

### 클래스(class)

- 클래스는 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류

### 인스턴스(Instance)
- 특정 클래스(class)의 실제 데이터 예시(instance)입니다. 
- 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 클래스의 인스턴스**

```python
# Person 클래스
class Person:
    pass

# yu는 Person 클래스의 인스턴스
yu = Person()
```
팁!!
> 일반 변수/함수명은 전부 소문자에, 띄어쓰기가 필요하면 _ 로 
> 
> ex)snake_case
> 
>클래스명은 첫글자 대문자에, 띄어쓰기 필요하면 또 대문자로  
> 
> ex) PascalCase, UpperCamelCase


## 속성(attribute)과 메서드(method)

객체의 속성(상태, 데이터)과 조작법(함수)을 명확히 구분해 봅시다.

| type         | attributes       | methods                                |
| -------------| ---------------- | -------------------------------------- |
| `complex`    | `.real`, `.imag` |              _                          |
| `str`        |       _          | `.capitalize()`, `.join()`, `.split()` |
| `list`       |       _          | `.append()`, `.reverse()`, `.sort()`   |
| `dict`       |       _          | `.keys()`, `.values()`, `.items()`     |


### 속성(attribute)

- 속성(attribute)은 객체(object)의 상태/데이터를 뜻함


**활용법**

```python
<객체>.<속성>
```

**예시**

```python
person.name
```

### 메서드(method)

- 특정 객체가 할 수 있는 행위(behavior)를 뜻 합니다.

**활용법**
```python
<객체>.<메서드>()
```

**예시**
```python
person.talk()
person.eat()
```

# 인스턴스(instance)

## 인스턴스(instance) 생성
* 정의된 클래스(`class`)에 속하는 객체를 해당 클래스의 인스턴스(instance)라고 함

* `Person` 클래스의 인스턴스는 `Person()`을 호출함으로써 생성

* `type()` 함수를 통해 생성된 객체의 클래스를 확인할 수 있음


**활용법**


```python
# 인스턴스 = 클래스()
person1 = Person()
```

- `person1`은 사용자가 정의한(user-defined) `Person`이라는 데이터 타입(data type)의 인스턴스입니다.


## 인스턴스 변수
* 인스턴스의 속성(attribute)
* 각 인스턴스들의 고유한 데이터
* 생성자 메서드에서 `self.변수명`로 정의(생성자 메서드는 뒤에 학습합니다.)
* 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당

---
**활용법**
    
```python
class Person:
    pass

p1 = Person()
p1.name = 'jack'
p1.age = 25
```


## 인스턴스 메서드

> 메서드란?
> - 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미함

* 인스턴스 메서드는 인스턴스가 사용할 메서드에 해당
* 클래스 내부에 정의되는 메서드는 기본적으로 인스턴스 메서드로 생성됨
* **메서드 호출시, 첫번째 인자로 인스턴스 자기자신에 해당하는 `self`가 전달됨**

**활용법**

```python
class MyClass:
    def instance_method(self, arg1, arg2, ...):
        ...

my_instance = MyClass()
# 인스턴스 생성 후 메서드를 호출하면 자동으로 첫 번째 인자로 인스턴스(my_instance)가 들어감
my_instance.instance_method(.., ..)  
```

- 메서드도 함수이기 때문에 추가적인 인자를 받을 수 있음
- 추가적인 인자를 받기 위해서는 아래와 같은 모습으로 코드가 작성되어야 함

```python
class MyClass:
    def method1(self):
        print('Hi')
    
    def method2(self, arg):
        print(arg)

예시
class Person:
    def talk(self):
        print('안녕!')

    def eat(self, food='치킨', *args):
        print(f'{food}를 얌냠')
        if args:  # 컨테이너 데이터가 값이 있다면,
            for arg in args:
                print(f'{arg}도 먹고싶긴 하다..')
p1 = Person()
p1.eat()
p1.eat('카레')
p1.eat('카레', '족발', '짜장면', '게장')
p1.talk()

= 치킨를 얌냠
카레를 얌냠
카레를 얌냠
족발도 먹고싶긴 하다..
짜장면도 먹고싶긴 하다..
게장도 먹고싶긴 하다..
안녕!
```

##  `self` 

> 인스턴스 자신(self)

* Python에서 인스턴스 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었음


* 보통 매개변수명으로 `self`를 첫번째 인자로 정의 (다른 이름도 가능하지만 추천하지는 않음)

### 생성자(constructor) 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
- 반드시 `__init__` 이라는 이름으로 정의

---
**활용법**

```python
class MyClass:
    def __init__(self):
        print('생성될 때 자동으로 호출되는 메서드')

ex)
class Person:
    def __init__(self, name, age, blood):
        self.name = name
        self.age = age
        self.blood = blood 

    def talk(self):
        print(f'안녕 내이름은 {self.name} 야')

p1 = Person('john', 20, 'A')
p2 = Person('eric', 22, 'O')

print(p1.name, p1.age, p1.blood)  #john 20 A
print(p2.name, p2.age, p2.blood)  # eric 22 O


p1.talk()  # 안녕 내이름은 john 이야
p2.talk()  # 안녕 내이름은 eric 이야
```

- 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있음


### 소멸자(destructor) 메서드
- 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수
- 반드시 `__del__` 이라는 이름으로 정의

---

**활용법**

```python
# 소멸자 정의
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
    
# 소멸자 활용
del 인스턴스
```

## 속성(Attribute) 정의

- 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터를 의미합니다.

- `self.<속성명> = <값>` 혹은 `<인스턴스>.<속성명> = <값>`으로 설정합니다

---
**활용법**

```python
# Person 클래스는 name이라는 속성이 정의
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')
# 인스턴스 속성의 값을 변경할 수도 있음
p1.name = 'yu'
p1.talk()
= 안녕, 나는 yu

```
- 속성 정의는 꼭 생성자(__init__) 메서드에 작성해야 하지는 않지만, 일반적으로 생성자 메서드에 많이 작성함
- 생성자 메서드를 통해 생성과 동시에 인스턴스 속성에 값을 할당할 수 있기 때문

## 매직(스페셜) 메서드
- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불림
- 매직(스페셜) 메서드 형태: `__someting__`
```python
 '__str__(self)',
 '__len__(self)',
 '__repr__(self)',
 '__lt__(self, other)',
 '__le__(self, other)',
 '__eq__(self, other)',
 '__ne__(self, other)',
 '__gt__(self, other)',
 '__ge__(self, other)',
```

### `__str__(self)` 

```python
class Person:
    def __str__(self):
        return '객체 출력(print)시 보여줄 내용'
```

- 특정 객체를 출력(`print()`) 할 때 보여줄 내용을 정의할 수 있음
> dir('')
> 문자열 인스턴스가 활용 가능한 메서드 확인 가능
```python
활용법
# 객체 <= 메서드 => 객체

# 1 + 2

(1).__add__(2)

# [1, 2, 3][1]
[1, 2, 3].__getitem__(1)

# 3 > 2

# gt => Greater Than
# gte => Greater Than or Eqaul
(3).__gt__(2)
(2).__gt__(3)

# lt => less than

# eq => equal
```

# 클래스 (class)

> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드

|클래스| 제품의 설계도|
|--|--|
|객체|설계도로 만든 제품|
|속성 |클래스 안의 변수|
|메서드|클래스 안의 함수|
|생성자 | 객체를 만들 때 실행되는 함수|
|인스턴스 |메모리에 살아있는 객체| 



## 클래스(Class) 생성

* 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능

* `<클래스의 이름>`은 `PascalCase`로 정의

* 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 **속성(attribute)** 정의된 함수는 **메서드(method)**로 부름

---

**활용법**

```python
class <클래스이름>:
    <statement>
```

```python
class ClassName:
    statement
```

## 클래스 변수
* 클래스의 속성(attribute)
* 모든 인스턴스가 공유
* 클래스 선언 내부에서 정의
* `클래스.변수명`으로 접근 및 할당

---

**활용법**
```python
class Circle:
    pi = 3.14
    
print(Circle.pi)

c1 = Circle()
c2 = Circle()
c1.pi, c2.pi
```

## 클래스 메서드(class method)
* 클래스가 사용할 메서드에 해당
* `@classmethod` 데코레이터를 사용하여 정의
* **메서드 호출시, 첫 번째 인자로 클래스 `cls`가 전달됨**

---

**활용법**

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...

# 자동으로 첫 번째 인자로 클래스(MyClass)가 들어감
MyClass.class_method(.., ..)  
```


## 스태틱 메서드(static method)
* 클래스가 사용할 메서드에 해당
* 인스턴스와 클래스의 속성과 무관한 메서드
* `@staticmethod` 데코레이터를 사용하여 정의
* **호출시, 어떠한 인자도 자동으로(`self`, `cls`)전달되지 않음**
* 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용


---

**활용법**

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        ...

MyClass.static_method(.., ..)
```


## 인스턴스와 클래스 간의 이름 공간 (namespace)

* 클래스를 정의하면 클래스와 해당하는 이름 공간이 생성됨
* 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간이 생성됨
* 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색한다
```python
class Person:
    # class var
    spices = 'human'
    
    # instance method
    def __init__(self, name):
        # instance var
        self.name = name

        
p1 = Person('Hong')
p2 = Person('Choi')
```
```python
# 변수는 LEGB 순으로 찾고
# 객체의 속성값(attr)과 메서드(method)는 instance => class => 상위 class ... 으로 찾는다.

a = 100

class Sample:
    a = 1

    def func(self):
        b = 2
        return a + b  # 102
        return self.a + b  # 3

s = Sample()
s.func()
= 3
```

# 비교 정리
### 인스턴스와 메서드
- 인스턴스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있다
    - 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다

```python
class MyClass:
    
    def instance_method(self):
        return 'instance method: ', self
    
    @classmethod
    def class_method(cls):
        return 'class method: ', cls
    
    @staticmethod
    def static_method():
        return 'static method'
```


### 클래스와 메서드
- 클래스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있음
    - 클래스에서 인스턴스 메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계함 (클래스 메서드와 정적 메서드)
    - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의합니다.
    - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의한다
        - 정적 메서드는 `cls`, `self`와 같이 묵시적인 첫번째 인자를 받지 않기 때문

### 예제
```python
class Circle:
    import math
    pi = math.pi
    
    # init
    def __init__(self, r):
        self.r = r
        
    # get_perimeter => 원의 둘레를 구하는 메서드  (2 pi r)
    def get_perimeter(self):
        return 2 * self.pi * self.r 
    
    # get_area => 원의 넓이를 구하는 메서드  (pi r**2)
    def get_area(self):
        return self.pi * self.r**2

c1 = Circle(3)  # 반지름이 3인 원
# c1.r => 3
c2 = Circle(5)  # 반지름이 5인 원
# c2.r => 5

c1.get_perimeter()  # c1의 둘레
c2.get_area()  # c2 면적 

# 반지름이 3, 5, 7, 8, 10 인 원들의 넓이의 합을 구하시오.
rs = [3, 5, 7, 8, 10]
total = 0

for r in rs:
    c = Circle(r)
    total += c.get_area()

total
```

## OOP의 핵심 개념
- 추상화 (Abstraction)
- 상속 (Inheritance)
- 다형성 (Polymorphism)
- 캡슐화 (Encapsulation)

### 추상화(Abstraction)란?

- 객체 지향 프로그래밍에서의 추상화는 세부적인 내용은 감추고 필수적인 부분만 표현하는 것을 뜻합니다.
- 현실 세계를 프로그램 설계에 반영하기 위해 사용됩니다.
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용합니다.
```python
# 학생(Student)을 표현하기 위한 클래스를 생성합니다.
class Student:
    
    def __init__(self, name, age, score):
        self.age = age
        self.name = name
        self.score = score
        
    def talk(self):
        print(f'안녕하세요, {self.name}입니다.')
        
    def study(self):
        self.score += 1
# 선생(Teacher)을 표현하기 위한 클래스를 생성합니다
 class Teacher:
    
    def __init__(self, name, age, money):
        self.age = age
        self.name = name
        self.money = money
        
    def talk(self):
        print(f'안녕하세요, {self.name}입니다.')
        
    def teach(self):
        self.money += 100

# Person이라는 클래스를 통해 추상화를 해봅시다.
class Person:

    def __init__(self, name, age, money):
        self.age = age
        self.name = name

    def talk(self):
        print(f'안녕하세요, {self.name}입니다.'
```
        

### 상속(Inheritance)이란?


클래스에서 가장 큰 특징은 `상속`이 가능하다는 것입니다. 

부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아집니다.

---

**활용법**


```python
class ChildClass(ParentClass):
    <code block>
```

```python
# Person 클래스를 정의해 보겠습니다.

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
    def talk(self):
        print(f'안녕하세요, {self.name}입니다.')

p1 = Person('kim', 30)
p1.talk()

# Person 클래스를 상속받아 Student 클래스를 만들어 보겠습니다.
class Student(Person):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
```

### `issubclass(class, classinfo)`

* class가 classinfo의 subclass인 경우 `True`를 반환합니다.

###### `isinstance(object, classinfo)`
```python
# Student 클래스와 Person 클래스가 상속관계인지 확인(클래스 상속 검사)
# issubclass(자식클래스, 부모클래스)

issubclass(Student, Person)
= false

# s1이 Student 클래스의 인스턴스인지, s1이 Person 클래스의 인스턴스인지 확인
# isinstance(인스턴스, 클래스)

print(isinstance(s1, Student))
print(isinstance(s1, Person))
= True
False
```
```python
활용 
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
        
p1 = Person('홍교수', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')

s1.greeting()
```

* object가 classinfo의 인스턴스거나 subclass인 경우 `True`를 반환합니다.


### `super()`

* 자식 클래스에 메서드를 추가로 구현 가능

* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용 가능

---

**활용법**


```python
class ChildClass(ParentClass):
    def method(self, arg):
        super().method(arg) 


class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # 부모 클래스의 __init__ 함수를 이 자리에서 실행
        super().__init__(name, age, number, email)
        self.student_id = student_id
        
        
p1 = Person('홍교수', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```

## 다형성(Polymorphism)이란?

- 여러 모양을 뜻하는 그리스어로, 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 뜻함
- 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 응답될 수 있음

### 메서드 오버라이딩
> Method Overriding(메서드 오버라이딩): 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

* 상속 받은 메서드를 `재정의`할 수도 있습니다. 
* 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어씁니다.
* `__init__`, `__str__`의 메서드를 정의하는 것 역시, 메서드 오버라이딩
* 
```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def talk(self):
        print(f'안녕, {self.name}')

# talk 메서드를 재정의(override)합니다.

class Soldier(Person):
    def __init__(self, name, age, number, email, army):
        super().__init__(name, age, number, email)
        self.army = army

    def talk(self):
        print(f'충성! 상병 {self.name}!')
```
### 캡슐화(Encapsulation)란?

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단하는 것
  - 예시: 주민등록번호
  
- 다른 언어와 달리 파이썬에서 캡슐화는 암묵적으로는 존재하지만, 언어적으로는 존재하지 않음

---

**접근제어자의 종류**
- Public Access Modifier
- Protected Access Modifier
- Private Access Modifier

|접근제어자|문법|의미|
|--|--|--|
|public|name|외부로부터 모든 접근 허용|
|protected|_name|자기 클래스 내부 혹은 상속받은 자식 클래스에서만 접근 허용|
|private|__name|자기 클래스 내부의 메서드에서만 접근 허용
### Public Member

- 언더바가 없이 시작하는 메서드나 속성들이 이에 해당
- 어디서나 호출 가능합니다.
- 하위 클래스에서 메서드 오버라이딩을 허용
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지

### Protected Member

- 언더바 1개로 시작하는 메서드나 속성들이 이에 해당
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
- 하위 클래스에서 메서드 오버라이딩을 허용

# Person 클래스를 재정의해봅시다.
# 실제 나이(age)에 해당하는 값을 언더바 한 개를 붙여서 Protected Member로 지정하였습니다.

### Private Member

- 언더바 2개로 시작하는 메서드나 속성들이 이에 해당
- 본 클래스 내부에서만 사용이 가능
- 하위 클래스 상속 및 호출이 불가능
- 외부 호출이 불가능

### 다중 상속
* 두개 이상의 클래스를 상속받는 경우, 다중 상속이 됩니다.
    * 상속 받은 모든 클래스의 요소를 활용 가능
    * 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정
```python
# Person 클래스를 정의합니다.
# Person 클래스는 생성자에서 인스턴스 변수로 name을 설정합니다.

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

ex) 
class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        print('어푸어푸')

m1 = Mom('봉미선')
m1.swim()
m1.greeting(), m1.gene

class Dad(Person):
    gene = 'XY'
    
    def walk(self):
        print('성큼성큼')
        
d1 = Dad('신형만')
d1.walk()
d1.greeting(), d1.gene


#다중상속

class FirstChild(Dad, Mom):
    def swim(self):
        print('첨벙첨벙')
        
    def dance(self):
        print('부리부리')

# 상속 순서 재정의 가능
class SecondChild(Mom, Dad):
    
    def cry(self):
        print('응애')

```

### 상속관계에서의 이름 공간과 MRO (Method Resolution Order)

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.
    * 인스턴스 -> 자식 클래스 -> 부모 클래스
    
- MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드

---

**활용법**


```python
ClassName.__mro__

# 또는
ClassName.mro()
```

```python


class Mom:
    def walk(self):
        print('사뿐사뿐')
        
        
class Dad:
    def walk(self):
        print('저벅저벅')


class Daughter(Mom, Dad):
    pass


class Son(Dad, Mom):
    pass
```