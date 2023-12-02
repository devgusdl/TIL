from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField(default='')
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    cgpa = models.FloatField()


class Professor(models.Model):
    name = models.CharField(max_length=10)
    major = models.CharField(max_length=100)
    room = models.TextField()
    year = models.IntegerField()


# $ python manage.py makemigrations <app_name>
# $ python manage.py migrate <app_name>

if __name__ == '__main__':
    pass
    # CRUD

    # 생성 Create
    s = Student()
    s.name = '김학생'
    s.major = '컴공'
    s.age = 25
    s.address = '서울'
    s.cgpa = 3.7
    s.save()

    Student.objects.create(
        name='박학생',
        major='경영',
        age=22,
        address='부산',
        cgpa=3.3
    )

    # 조회 Read(Retrieve)
    # 1. 전체 조회
    students = Student.objects.all()
    for student in students:
        print(student.pk, student.name, student.major)
    # 2. 단일 조회
    Student.objects.get(id=1)  # 컬럼명
    s1 = Student.objects.get(pk=1)  # Primary Key 역할
    print(s1.name, s1.address, s1.cgpa)


    # 수정 Update
    s1 = Student.objects.get(pk=1)
    s1.cgpa = 4.0
    s1.age = 26
    s1.save()

    # 삭제 Delete(Destroy)
    s1 = Student.objects.get(pk=1)
    s1.delete()

    # 실습
    '''
    1. 데이터 입력하기
    2. 전체 조회 및 단일조회(id 말고 다른 조건으로도)
    3. choi 교수의 year 3으로 바꾸기
    4. kim 교수의 room k102 로 바꾸기
    5. lee 교수 삭제하기
    6. park 교수 삭제하기
    '''
    # 1
    Professor.objects.create(name='kim', major='CSE', room='k101', year=5)
    Professor.objects.create(name='park', major='MAN', room='e554', year=10)
    Professor.objects.create(name='lee', major='KOR', room='d331', year=4)
    Professor.objects.create(name='choi', major='CSE', room='p224', year=2)
    # 2
    Professor.obects.all()
    Professor.objects.get(name='kim')
    Professor.objects.get(pk=1)
    
    # 3
    p = Professor.objects.get(name='choi')
    p = Professor.objects.get(pk=4)
    p.year = 3
    p.save()

    # 4
    p = Professor.objects.get(name='kim')
    p.year = 'k102'
    p.save()

    # 5
    p = Professor.objects.get(name='lee')
    p.delete()

    # 6
    p = Professor.objects.get(name='park')
    p.delete()

