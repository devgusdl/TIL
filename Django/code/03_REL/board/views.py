# board/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


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
    form = CommentForm()
    # article에 request.user 가 좋아요를 눌렀는가?
    is_like = article.like_users.filter(pk=request.user.pk).exists()

    return render(request, 'board/detail.html', {
        'article': article,
        'form': form,
        'is_like': is_like,
    })  


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
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
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('board:detail', article.pk)


@login_required
@require_POST
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.user != comment.user:
        return redirect('board:detail', article.pk)
    
    comment.delete()
    return redirect('board:detail', article.pk)

@login_required
@require_POST
def like(request, pk):
    # 모델링 => 뷰함수 => UI / 시나리오
    # detail.html 에 버튼을 만든다 => 여기 함수에 진입한다. => 다시 detail로 리다이렉트

    article = get_object_or_404(Article, pk=pk)
    user =  request.user

    
    # if user in article.like_users.all():  # Python
    
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)  # 좋아요 취소
    else:
        article.like_users.add(user)  # 좋아요 추가


    return redirect('board:detail', article.pk)
