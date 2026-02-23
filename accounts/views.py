from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        messages.success(request, f'Seja bem-vindo de volta, {user.username}!')
        return redirect('dashboard_index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Seja bem-vindo de volta, {user.username}!')
            return redirect('dashboard_index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'accounts/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST.get('username'),
                                        email = request.POST.get('email'),
                                        password = request.POST.get('password'))
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    return render(request, 'accounts/register.html')