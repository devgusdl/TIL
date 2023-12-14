from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}) {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    # 아래 ActorMovie 클래스 정의를 이 한줄로 대체 가능
    actors = models.ManyToManyField(Actor, related_name='movies')  # movie => actors 로 접근 / actor => movies로 접근

    def __str__(self):
        return f'{self.pk} => {self.title}'


# class ActorMovie(models.Model):
#     actor = models.ForeignKey(Actor)
#     movie = models.ForeignKey(Movie)


if __name__ == '__main__':
    # python manage.py shell_plus
    m1 = Movie.objects.get(pk=1)
    m2 = Movie.objects.get(pk=2)
    m3 = Movie.objects.get(pk=3)
    m4 = Movie.objects.get(pk=4)
    m5 = Movie.objects.get(pk=5)

    a1 = Actor.objects.get(pk=1)
    a2 = Actor.objects.get(pk=2)
    a3 = Actor.objects.get(pk=3)
    a4 = Actor.objects.get(pk=4)
    a5 = Actor.objects.get(pk=5)
    
    # M:N 관계 추가
    # 영화에 배우추가
    m1.actors.add(a1)
    m1.actors.add(a2, a4)
    m2.actors.add(a4)
    m2.actors.add(a5)
    # 배우에 영화추가 (related_name 때문에 movies)
    a2.movies.add(m3)
    a2.movies.add(m4)
    a3.movies.add(m3, m4, m5)
    a4.movies.add(m1, m2, m5)

    # M:N 삭제 코드 (아래 2개중 택1)
    a2.movies.remove(m3)
    m3.actors.remove(a2)

    # M:N 조회
    a3.movies.all()
    m5.actors.all()

    # m3의 출연진 중 첫번째 출연진의 필모
    m3.actors.all()[0].movies.all()

