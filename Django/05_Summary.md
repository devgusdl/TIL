#  1:N (일대다 관계)
1 : N 관계는 한 쪽 엔티티가 관계를 맺은 엔티티 쪽의 여러 객체를 가질 수 있는 것을 의미합니다.
이 관계는 매우 흔한 방식이며, 실제 DB를 설계할 때 자주 쓰이는 방식입니다.

한 사람이 게시물여러개 작성할수있게 하고 몇번째 사람이 적었는지 확인
-	실습
1.	User : Student = 1 : N
2.	crud App > Model Student 에 작성자(user) 정보 추가(FK)
3.	forms.py  에서 form 수정(user정보는 HTML에서 보이지 않도록)
4.	views.py 에서 학생정보 저장시 작성자(user)를 저장할 수 있도록 변경
5.	detail.html 과 index.html 에서 학생정보 작성자를 확인할 수 있도록 변경

# Model
```python
from django.db import models
from django.contrib.auth import get_user_model
# user class에 modelclass를 가져와주는 함수
User = get_user_model()

# User 클래스를 사용할 경우.
# 1. 모델간 관계설정시에는 settings.AUTH_USER_MODEL 사용
# 2. 그 외(form 생성등)에는 get_user_model() 함수 사용

class Student(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
```
# Form
Exclude =  ~ 항목만 빼고 
```python
    class Meta:
        model = Student
        exclude = ('user',)
        # fields = '__all__' all에서 빼는게 기본 값
```
# View
```python
@require_http_methods(['GET','POST'])
def create(request):
    if request.method =='GET':
        form = StudentForm()
   
    elif request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            # user 정보 없음 => student 저장 불가능 => 저장 직전 STOP
            student = form.save(commit=False)
             # 이 student의 작성자 = 이 요청을 보낸 사용자
            student.user = request.user
            student.save()
            return redirect('crud:detail', student.pk)
    
    return render(request, 'crud/form.html', {
            'form': form,
        })
    
```
# Detail
```python
<h1>{{ student.name }}</h1>
<h2>{{article.user}}</h2>
# article.user이라고 표현함
```

