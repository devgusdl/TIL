# Django CRUD
CRUD = create, read, update, delete


-  실습
1. Project PRACTICE
2. App crud 를 만들고 진행
3. model Student 클래스 생성
   1. name => CharField(100)
   2. age => IntegerField
   3. major => CharField(10)
   4. description => TextField
4. 데이터 베이스 반영(migrate)
5. URL 패턴 세팅
   1. school/new/ => new => new.html (학생 정보 입력 화면)
   2. school/create/ => create => 실제 학생 저장 => detail 로 redirect
   3. school/ => index => index.html (전체 학생 조회)
   4. school/1/ => detail => detail.html (단일 학생 조회)
   5. school/1/edit/ => edit => edit.html (학생 수정 입력 화면)
   6. school/1/update/ => update => 학생 정보 수정 저장 => detail redirect
   7. school/1/delete/ => delete => 학생 삭제 => index redirect
6. HTML 은 base2.html 을 만들고 확장해서 사용
7. 하드코딩된 url -> 변수url로 변경


## Project urls
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns =[
   path('admin/'admin.site.urls),
   path('board/',include('board.urls')), # app urls와 연결
]
```

## App urls
```python
urlpatterns = [
    path('new/', view.new),  # new로 들어오면(board/new/), view로 간다(= view와 연결)
    -
    -
    path('<int:pk>/',views.detail),
    path('<int:pk>/edit',views.edit), 
    path('<int:pk>/update',views.update),
    path('<int:pk>/delete',views.delete),
]    # <int:pk> 추가해야한다 왜냐하면 하나하나씩 삭제하기 때문이다.예를들어 1번게시물을 삭제요청하면 그 1번을 삭제하기위해선 detail과 숫자가 같아야한다.
```


### 변수 설정
추가적으로 하드코딩된 URL변수사용하는 방법을 적어보자면
```python
# <app_name>:<pattern_name>
app_name  = 'crud'

urlpatterns = [
    path('new/', view.new, name='new'), 
    -
    -
    path('<int:pk>/',views.detail, name='detail'),
    path('<int:pk>/edit',views.edit, name='edit'), 
    path('<int:pk>/update',views.update, name='update'),
    path('<int:pk>/delete',views.delete,name='delete'),

``` 
`이런식으로 표현하면 ex) crud:new 라고 된다 다음으로 바꿔야하는곳 3개`

 ` 1. html에 a 태그`

 ` 2. html에 action`

 ` 3. view.py에 redirect하는 곳`
## model
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    description = models.TextField()
```


## Settings
```python
TEMPLATES = [
    {
        'BACKEND': ~~~~~~, 
        'DIRS': [BASE_DIR / 'templates'],
        # w장고는 기본적으로 앱안에 templates라는 폴더만 찾는데 공용템플릿을 통해 base.html 쓰기위해서 적는 것 = template파일을 찾을 디렉토리를 알려주기 위함
```

## Base.html
```python
<body>
  <nav>
    <ul>
      <li> # 이렇게하고 사이트 들어가면 2개의 항목이 표시됌 = index
        <a href= "/board/">Home</a>
      </li>
      <li>
        <a href= "/board/new/">NEW</a>
      </li>
    </ul>
  </nav>
  {% block content %}
  
  {% endblock content %}
</body>
</html>
```

## views
여기있는 redirect('crud:detail',student.pk) 이것도 변수를 설정해서 한 것
```python
from django.shortcuts import render, redirect
from .model import Student

# CREATE
def new(request):
    # 새로운 student를 생성하기 위한<form>(html) =>작성데이터는 create함수로 보내야 함
    return render(request,'crud/new.html')

def create(request):
    student = Student()
    student.name = request.GET['student_name']
    ~
    ~
    ~
    student.save() # 저장됨! => id(pk)가 생김
    # 다른곳으로 넘어감 '/board/' = 홈으로
    return redirect('crud:detail',student.pk)

# READ
def index(request):
    #전체 학생 목록 확인
    students = Student.objects.all()
    return render(request,'crud/index.html',{
        'students' : students,
    })
    
def detail(request,pk):
    # pk = pk 라고하면 1일때 1게시물, 2일때 2게시물 조회 가능
    student = Student.objects.get(pk=pk) 
    return # 위에랑 똑같음 crud/detail

# UPDATE
def edit(request, pk):
    # 새로운 student를 생성하기 위한<form>(html) =>작성데이터는 create함수로 보내야 함
    return # 위에랑 똑같음 crud/edit 

def update(request, pk):
    # edit.html에서 넘어온 데이터를 실제 저장
    student = Student()
    student.name = request.GET['student_name']
    ~ age
    ~ major
    ~ decription
    student.save() # 저장 됨! =>id(pk)가 생김

# DELETE
    return redirect('crud:detail',student.pk)
def delete(request, pk):
    #URL에 넘어온 pk에 해당하는 학생정보 삭제
    student = Student.objects.get(pk=pk)
    student.delete()
    # view 에서 redirect => '<app_name>:<name>'
    return redirect ('crud:index')
    # DTL(템플릿) {% URL '<app_name>:name' %}
```


## html
```python
html

{% extends "base.html" %}
<h1> New student</h1>

<from action ={% url"crud:create" %}>

{% block contect %}
# student.pk로 바꾼 이유는 변수를 사용하기 위해서이다
# ㅇ
<a href ="/school/{{student.pk}}/edit/">
<button oneclick="return confirm('삭제?')">삭제</button>
</a>

{% endblock content %}

```