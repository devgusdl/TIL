# Django form

- 실습

PRACTICE > crud app 에서 ModelForm 사용하기
1. crud/forms.py 생성
2. forms.py 에 StudentForm 이라는 모델폼 생성
    1. 모델은 Student
    2. 필드는 모든 필드
3. new.html 과 edit.html 에서 `<form>` 의 제출 방식(method) 를 모두 POST 로 교체
    - 토큰 잊지 않기
4. new.html 과 edit.html 에서 `<input>` 요소들 모두 form 에서 출력하도록 교체
5. create 와 update 에서 사용자 입력을 검증 및 통합(url과 함수 둘 다)
    1.  유효할 경우에만 저장.
    2.  유효하지 않을 경우, 에러메세지와 함꼐 html 다시 렌더
6. 단일 객체 찾을 경우 get_object_or_404 로 바꾸기

7. 함수마다 요청 메서드 데코레이터 붙이기 (require_safe, require_POST, require_http_methods)
8. delete 요청 POST 로 바꾸기

- 배운 것 요약
RACTICE > crud  <=> MODEL > board
1. create 함수 / update 함수
2. new.html 과 edit.html 병합
3. URL 하나로 바뀐거
4.  form 태그 액션 사라짐

 ## forms
 ```python
 # board/forms.py
from django import forms
from .models import Article

# 0. (fields 에 적힌 컬럼에 대해서만)
# 1. 입력 데이터 검증 => 저장
# 2. HTML(input/textarea/...)을 생성
class ArticleForm(forms.ModelForm):
    # django 에서 문자열을 검증할 필드
    title = forms.CharField(min_length=2, max_length=40)
    content = forms.CharField(
        min_length=5,
        # forms.CharField 는 기본값이 input type text
        # widget을 통해 HTML 코드도 바꿀 수 있음
        widget=forms.Textarea(
            # class 주는 코드 예시
            attrs={'class': 'my-class'}
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('content', )
 ```
 
 ## Views
 ```python
 # board/views.py
 # get_object_or_404는 데이터베이스에서 객체를 가져오거나 404 오류를 발생시킵니다.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST,require_http_methods

from .models import Article
from .forms import ArticleForm
# 이 함수는 데코레이터로, HTTP 요청 메서드가 GET 또는 POST인 경우에만 실행됩니다. GET 요청은 페이지를 표시하고 POST 요청은 양식을 처리합니다.
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'GET': # 기존 new 코드
        form = ArticleForm()  # input tag 대신 생성

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid(): # 검증
            article = form.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form': form,
    })


# Read
@require_safe # 영향을주지않는 읽기만 세이프하다
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })  

@require_http_methods(['GET','POST'])
def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,pk=pk)  
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


# Delete``
@require_POST #이제부터 post만 받겠다
def delete(request, pk):
    article = get_object_or_404(Article,pk=pk)
    # article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')
 ```


 ## form.html
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