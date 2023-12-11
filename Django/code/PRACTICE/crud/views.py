from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Student, Reply
from .forms import StudentForm, ReplyForm

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('crud:detail', student.pk)
    else:
        form = StudentForm()
    
    return render(request, 'crud/form.html', {
        'form': form,
    })
    

@require_safe
def index(request):
    # 전체 학생 목록 확인
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students': students,
    })



@require_safe
def detail(request, pk):
    # 학생 상세 정보 확인
    student = get_object_or_404(Student, pk=pk)
    form = ReplyForm()
    return render(request, 'crud/detail.html', {
        'student': student,
        'form': form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if student.user != request.user:
        return redirect('crud:index')

    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'crud/form.html', {
        'form': form,
    })
    

@login_required
@require_POST
def delete(request, pk):

    if student.user != request.user:
        return redirect('crud:index')
    
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('crud:index')


@login_required
@require_POST
def create_reply(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = ReplyForm(data=request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.user = request.user
        reply.student = student
        reply.save()
    return redirect('crud:detail', student.pk)


@login_required
@require_POST
def delete_reply(request, pk, reply_pk):
    student = get_object_or_404(Student, pk=pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    
    if reply.user == request.user:
        reply.delete()

    return redirect('crud:detail', student.pk)
