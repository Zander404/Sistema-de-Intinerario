from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Rote

# Create your views here.

def index(request):
    return render(request, 'horarios/index.html')


def intinerario(request):
    data = Rote.objects.all().order_by('box')
    paginator = Paginator(data, 42)
    print(paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'horarios/intinerario.html', {'page_obj': page_obj, 'total_pages': paginator.num_pages})


def info(request, box):
    data = Rote.objects.get(box=box)

    horarios = list(zip(data.weekly_time, data.alternative_time))
    
    # return render(request, 'horarios/info.html', {'dados': data})
    return render(request, 'horarios/info.html', {'info': data, "horarios": horarios})



def institucional(request):
    return render(request, 'horarios/institucional.html')

def transporte(request):
    return render(request, 'horarios/transporte.html')

def contato(request):
    return render(request, 'horarios/contato.html')