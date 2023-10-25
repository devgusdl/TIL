# login,signup,logout
- 실습
1. get_object_or_404
2. 함수마다 요청 메서드 데코레이터 붙이기 (require_safe, require_POST, require_http_methods)
3. delete 요청도 DB에 변화를 주기때문에 POST 로 바꾸기
4. Admin 페이지와 python manage.py createsuperuser
5. django 의 내장 회원 관리 시스템의 존재
   1. 사용자 커스터마이즈 하지 않으면 Model과 Form 정의 불필요
   2. django.contrib.auth.forms 에 회원가입/로그인 Form 이미 존재
   3. django.contrib.auth 에 로그인/로그아웃 함수 이미 존재
   
6. python manage.py makemigrations , python manage.py migrate 로 한번에 진행
7. accounts 앱 => 회원관리 전반을 담당
8. 기존 코드와 굉장히 유사함
9. request.user 의 존재와
10. AnonymousUser
회원가입/로그인의 실제 의미 (쿠키/세션)
+ .gitignore 와 https://gitignore.io


## views
```python
from django.shortcuts import render, redirect #이거 꺼내야함
from django.views.decorators.http import require_http_methods

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout # 쿠키세팅
# usercreationform 은 실제 테이블의 데이터를 쓰는것
# authentication은 그렇지 않다 model폼이 아님, 테이블에 뭔갈 쓰는게 아니다보니 save가 없다
# 로그인

@require_http_methods(['GET','POST'])
def signup(request):
    # 요청보낸 사용자가 인증되었다(로그인했다)=>바로 돌려보내기
    if request.user.is_authenticated: 
        return redirect('crud:index')
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST) # POST사용자가 데이터를 던진상황에서는 form에다가 사용자가 던진데이터 받아서
        if form.is_valid(): # 유효성 체크 하고
            user = form.save() # 괜찮으면 세이브
            auth_login(request,user)
            return redirect('crud:index') 
    else:
        form = UserCreationForm() #GET요청이 들어왔을때는 폼하나 만들고

    return render(request, 'accounts/signup.html', {
       'form': form,
    })    # 안괜찮으면 이거
    
@require_http_methods(['GET','POST'])
def login(request):
    # 요청 보낸 사용자가 인증되었다(로그인했다)면 => 바로 돌려보내기
    if request.user.is_authenticated: 
        return redirect('crud:index')

    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST) # 정보가 입력된것, 로그인할때 아이디패스워드 검증까지만
        if form.is_valid(): # 아이디패스워드 맞냐
            user = form.get_user() # 아이디패스워드에 맞는 사용자 객체를 꺼내와야함 
            # 쿠키(팔찌)세팅
            auth_login(request,user) # 장고가 팔찌채워줘야하는 함수가 있는데 함수가 인자받아야하는게 두개임 하나는 리퀘인증받은스트 , 하나는 방금  사용자
            return redirect('crud:index')            
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{
        'form' : form,
    })
    
```
## Project urls
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('util/', include('util.urls')),
    path('univ/', include('crud.urls')), # 앱의urls와 연결
    path('accounts/',include('accounts.urls')),
]

```
## App urls
```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', views.signup, name = 'signup'),
    # /accounts/login/
    path('login/',views.login, name = 'login'),
    # /accounts/logout/
    path('logout/', views.logout, name = 'logout'),
]

```

## html(login,signup)
```python
{% extends "base1.html" %}

{% block content %}

<form method ='POST'>
    {% csrf_token %}
    {{form.as_p}}
<p> # 로그인 회원가입만 다름
    <button>로그인</button>
</p>
</form>

{% endblock content %}
```

## base.html
```python
 <body>
  <nav>
    <ul>
      <li>       
      <a href="{% url "crud:index" %}">Home</a>
      </li>
      {% comment %} 요청 보낸 사용자가 로그인하지 않았다면 {% endcomment %}
      {% if not request.user.is_authenticated %}
      <li>
        <a href="{% url "accounts:login" %}">Login</a>
      </li>
      <li>
        <a href="{% url "accounts:signup" %}">Signup</a>
      </li>
      {% comment %} 요청 보낸 사용자가 로그인 했다면 {% endcomment %}
      {% else %}
      <li>
        <a href="{% url "crud:create" %}">New</a>
      </li>
      <li>
        <a href="{% url "accounts:logout" %}">{{request.user}} - Logout</a>
      </li>
      {% endif %}
    </ul>
  </nav>
  {% block content %}
  
  {% endblock content %}
</body>
</html>
```