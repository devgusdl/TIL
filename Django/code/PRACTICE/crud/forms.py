from django import forms
from .models import Student, Reply


class StudentForm(forms.ModelForm):
    # 상수(값이 초기화/할당 이후 절대 변하면 안된다는 뜻)
    CHOICES = [
        ('SOC', '사회학'),
        ('POL', '정치외교학'),
        ('PSY', '심리학'),
        ('CSE', '컴퓨터공학'),
        ('BUS', '경영학'),
        ('CHE', '화학공학'),
    ]

    name = forms.CharField(min_length=1, max_length=10)
    age = forms.IntegerField(min_value=10, max_value=200)
    major = forms.ChoiceField(
        widget=forms.Select(),
        choices=CHOICES
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        min_length=5
    )

    class Meta:
        model = Student
        exclude = ('user', )


class ReplyForm(forms.ModelForm):
    CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    rank = forms.ChoiceField(
        widget=forms.Select(),
        choices=CHOICES
    )

    class Meta:
        model = Reply
        exclude = ('user', 'student',)