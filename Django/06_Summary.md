# 게시물 댓글 구현하기
-	실습 Practice
1.	Model Student
    1.	user : 작성자 추가하기
2.	Model Reply
    1.	user  : user 정보
    2.	student : student 정보
    3.	content : 내용(CharField)
    4.	rank : 평점(IntegerField)
3.	User: Student = 1 : N
4.	User : Reply = 1: N
5.	Student : Reply = 1: N
6.	학생 디테일 페이지에서 Reply 작성
7.	로그인 하지 않으면 Student CUD 불가능, Reply CD 불가능
8.	Reply 의 CRD
    1.	/univ/1/reply/create
    2.	/univ/1/reply/1/delete
    3.	조회는 학생 디테일 페이지에서 진행

# views
```python
# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

#로그인의 권한이 필요한 이유는 로그인없이도 막 적을
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()  # input tag 대신 생성

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # 저장하면 작성자 정보 없어서 에러 => 잠깐! 멈춰봐!(commit=False)
            article.user = request.user
            article.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form': form,
    })


@require_safe
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 댓글 작성용 HTML
    form = CommentForm()
    # 댓글 조회용
    # comments = article.comment_set.all() # 그 게시글의 댓글모두를 보겟다
    # 근데 이거detail에 적을수있음 -> detail.html
    return render(request, 'board/detail.html', {
        'article': article,
        'form': form,
    })  


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 작성자와 너가 같지않다면 나는 너를 리다이렉트 시킬거야
    if request.user != article.user:
        return redirect('board:detail', article.pk)

    
    if request.method == 'GET':
        form = ArticleForm(instance=article)

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete(request, pk):        
    article = get_object_or_404(Article, pk=pk)
    
    if request.user != article.user:
        return redirect('board:detail', article.pk)

    article.delete()
    return redirect('board:index')
    

# 로그인 안하고 get 요청 보냄
@login_required
@require_POST
def create_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False) # 당장세이브를 할 수 없음
        comment.article = article # 나 댓글인데 너의 게시글은 누구고, 작성자는 누구야가 필요함
        comment.user = request.user
        comment.save() # 그 후에 저장하는거임
    return redirect('board:detail', article.pk) #article.pk적기위해 위에 article = getobject 이거 쓰는거임

# pk가 필요한 이유는 112번에 article 116번 때문이다

@login_required
@require_POST
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return redirect('board:detail', article.pk)
    
    comment.delete()
    return redirect('board:detail', article.pk)
```



## App urls
```python
# board/urls.py
from django.urls import path
from . import views

# <app_name>:<pattern_name>
app_name = 'board'

urlpatterns = [

    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),

    # board/1/comments/create
    # views뒤에 그냥create라고 쓰면 위에있는 create와 겹치기 때문에 create_comment라고 쓴 것이다
    path('<int:pk>/comments/create/', views.create_comment, name='create_comment'),
    # board/1/comments/1/delete/
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    # url에 1이 필요한 이유는 comment를 찾기 위해서임
]
```


# Models
```python
# board/models.py
from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```




# Forms
```python
# board/forms.py
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    # django 에서 문자열을 검증할 필드
    title = forms.CharField(min_length=2, max_length=40)
    content = forms.CharField(
        min_length=5,
        widget=forms.Textarea(
            attrs={'class': 'my-class'}
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'content',)
        exclude = ('user', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', ) #이걸 잘못쓰면 다른사람이 남의 댓글을 쓸수있는 현상이 발생함
        # exclude = ('user', 'article')
```



# Detail.html
```python
{% extends "base.html" %}

{% block content %}
<h1>{{ article.title }}</h1>
<h2>{{ article.user }} </h2>

<p>
  {{ article.content }}
</p>

{% if article.user == request.user %} # 작성자와 현재 페이지를 보는 사람이 같을때만 보여주기(수정삭제)
<div>
  <a href="{% url "board:update" article.pk %}">
    <button>수정</button>
  </a>
</div>
<div>
  <form action="{% url "board:delete" article.pk %}" method="POST">
    {% csrf_token %}
    <button onclick="return confirm('진짜 삭제?')">
      삭제
    </button>
  </form>
</div>
{% endif %}

<hr>
# 다른 파일을 통해 연동할 수 잇어서 파일은 간략하게 축소할때 사용한다.
{% include "board/detail_comment.html" %}

{% endblock content %}
```

## include 함수
```python
{% if request.user.is_authenticated %} # 인증된 사용자한테만 보여줄거야
<form action="{% url "board:create_comment" article.pk %}" method="POST">
  {% csrf_token %} # 검증
  {{ form }} 
  <button>댓글작성</button>
</form>
{% endif %}

<div>
  <ul> # detail에서 조회하는것도 가능하다 set.all뒤에 소괄호 안씀
  {% for comment in article.comment_set.all %}
    <li> 
      {{ comment.user }} => {{ comment.content }}
    # 댓글을 작성하는자와 지금화면을보고있는 너가 같아야한다.
      {% if request.user == comment.user %}
      <form action="{% url "board:delete_comment" article.pk comment.pk %}" method="POST" style="display: inline-block;">
        {% csrf_token %} 
        <button onclick="return confirm('댓글 삭제?')">삭제</button>
      </form>
      {% endif %}
    </li>
  {% endfor %}
  </ul>
</div>
```
# Index.html
```python
{% extends "base.html" %}

{% block content %}
<h1>Index</h1>

<ul>
  {% for article in articles %}
  <li>
    <a href="{% url "board:detail" article.pk %}">
      {{ article.title }}
    </a>
  </li>
  {% endfor %}
</ul>
{% endblock content %}
```
# form.html
```python
{% extends "base.html" %}

{% comment %} templates/board/form.html {% endcomment %}

{% block content %}
<form method="POST">
  {% csrf_token %}

  {{ form.as_p }}

  <div>
    <button>제출</button>
  </div>
</form>
{% endblock content %}
```
