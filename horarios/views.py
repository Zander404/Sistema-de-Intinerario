from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Rote
from .forms import RoteForms


# -----------------------------ROTAS BASES-----------------------------------------

def index(request):
    return render(request, 'horarios/index.html')


def institucional(request):
    return render(request, 'horarios/institucional.html')


def transporte(request):
    return render(request, 'horarios/transporte.html')


def contato(request):
    return render(request, 'horarios/contato.html')


def intinerario(request):
    data = Rote.objects.all().order_by('box')
    paginator = Paginator(data, 42)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'horarios/intinerario.html', {'page_obj': page_obj, 'total_pages': paginator.num_pages})


def search_intinerario(request):
    query = request.GET.get('query', '')
    data = Rote.objects.filter(name__icontains=query) or Rote.objects.filter(box__icontains=query) if query else []
    paginator = Paginator(data, 42)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'horarios/intinerario.html', {'page_obj': page_obj, 'total_pages': paginator.num_pages})


def info(request, box):
    data = Rote.objects.get(box=box)

    horarios = list(zip(data.weekly_time, data.alternative_time))
    return render(request, 'horarios/info.html', {'info': data, "horarios": horarios})



# -----------------------------ROTAS ADMINS-----------------------------------------
# @login_required(login_url='login/')
def painel(request):
    return render(request, 'user/system.html')


## ----------------------ROTAS CRUD DE INTINERARIO----------------------------------
# @login_required(login_url='login/')
def create_rote(request):
    if request.method == 'POST':
        form = RoteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
        
        else:
            form = RoteForms()

        return render(request, 'crud/rote/form.html', {'form': form})


def read_rote(request):
    rotes = Rote.objects.all().order_by('id')
    pagination = Paginator(rotes, 30)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    return render(request, 'horarios/crud/rote/list.html', {'page_obj': page_obj, 'totla_pages': pagination.num_pages})


def detail_rote(request, pk):
    rote = get_object_or_404(Rote, pk=pk)
    return render(request, 'horarios/crud/rote/detail.html', {'rote': rote})

# @login_required(login_url='login/')
def update_rote(request, pk):
    rote = get_object_or_404(Rote, pk=pk)

    if request.method == 'POST':
        form = RoteForms(request.POST, instance=rote)
        if form.is_valid():
            form.save()
            return redirect('detail_rote',)
        
        else:
            form = RoteForms(instance=rote)

        return render(request, 'horarios/crud/rote/form.html', {'form': form})

# @login_required(login_url='login/')
def delete_rote(request, pk):
    rote = get_object_or_404(Rote, pk=pk)
    if request.method == 'POST':
        rote.delete()
        return redirect('list_rotes')
    
    return render(request, 'horarios/crud/rote/delete.html', {'rote': rote})

