from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserForm, LoginForm


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel')

        else:
            return render(request, 'user/index.html', {'form': form, 'errors': form.errors})

    else:
        form = UserForm()

    return render(request, 'user/index.html', {'form': form})




def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('painel')
            
            else:
                messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

