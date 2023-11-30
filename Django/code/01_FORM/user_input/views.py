from django.shortcuts import render


def hello(request, name):
    message = f'반갑습니다 {name}님!'
    return render(request, 'user_input/hello.html', {
        'message': message,
    })


def ping(request):
    return render(request, 'user_input/ping.html')


def pong(request):
    username = request.GET['username']
    password = request.GET['password']
    return render(request, 'user_input/pong.html', {
        'a': username,
        'b': password,
    })
    