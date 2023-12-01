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