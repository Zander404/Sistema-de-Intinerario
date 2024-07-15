from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Rote

# Create your views here.

def index(request):
    return render(request, 'horarios/index.html')


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



def institucional(request):
    return render(request, 'horarios/institucional.html')

def transporte(request):
    return render(request, 'horarios/transporte.html')

def contato(request):
    return render(request, 'horarios/contato.html')