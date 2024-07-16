from django.shortcuts import render, redirect
from .forms import UserForm

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



