from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Rote

# Create your views here.

def index(request):

    data = Rote.objects.all().order_by('box')
    paginator = Paginator(data, 42)
    print(paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'horarios/index.html', {'page_obj': page_obj, 'total_pages': paginator.num_pages})


def info(request, box):
    data = Rote.objects.get(box=box)

    horarios = list(zip(data.weekly_time, data.alternative_time))
    
    # return render(request, 'horarios/info.html', {'dados': data})
    return render(request, 'horarios/info.html', {'info': data, "horarios": horarios})