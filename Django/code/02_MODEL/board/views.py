# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST,require_http_methods

from .models import Article
from .forms import ArticleForm

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'GET':
        form = ArticleForm()  # input tag 대신 생성

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
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