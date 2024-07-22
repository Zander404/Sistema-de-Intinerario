from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
                return redirect('/painel/')
            
            else:
                messages.error(request, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})



@login_required(login_url='login/')
def user_list(request):
    user = User.objects.all().order_by('id')
    paginator = Paginator(user, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user/crud/list.html', {'page_obj': page_obj, 'total_pages': paginator.num_pages})


@login_required(login_url='login/')
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('detail_user', pk=user.id)
        
    else:
        form = UserForm(instance=user)

    return render(request, 'user/crud/form.html', {'form': form})

@login_required(login_url='login/')
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user/crud/detail.html', {'user': user})

@login_required(login_url='login/')
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
