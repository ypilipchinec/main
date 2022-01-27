from django.shortcuts import render
from django.db.models import Count
from django import template
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#models
from .models import *
from .forms import CamersForm

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg, '')

def get_paginate(page, get_query, number):
    
    paginator = Paginator(get_query, number)
    try:
        page_camers = paginator.page(page)
    except PageNotAnInteger:
        page_camers = paginator.page(1)
    except EmptyPage:
        page_camers = paginator.page(paginator.num_pages)
    return page_camers

def form_camers(request, type, id):
    if request.method == 'POST':
        form = CamersForm(request.POST)
        if form.is_valid():
            post = 'форму заполнил'
        else:
            post = 'форма неверна'
    else:
        post = 'пустая форма'
    form = CamersForm
    context = {
        'request': request.POST,
        'post': post,
        'type': type,
        'id': id,
        'form': form
    }
    return render(request, 'form_camers.html', context)

def show_camers(request, types):
    list_camers = camers.objects.filter(type=types)
    page = request.GET.get('page', 1)
    paginate = get_paginate(page, list_camers, 100)
    context = {
        'camers': paginate,
    }
    return render(request, 'show_camers.html', context)

def screens_status(request, names, status, created_at):
    """
    screens_status [show failed camers or screens]
    Args:
        request ([tuple]):
        names ([string]): [type of camers]
        status ([string]): [status camers]
        created_at ([datetime]): [datetime when screens creating]
    Returns:
        [list]: [select of where names, status, created_at some filteres]
    """ 
    
    check_date = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
    get_screens = files.objects.filter(name = names).filter(status=status).filter(create_at__contains = check_date).order_by('file')

    context = {
        'screens': get_screens,
    }
    return render(request, 'screens_status.html', context)


def index(request):
    get_camers = camers.objects.values('name').values('type').annotate(count=Count('id'))
    get_type = list()
    get_type = files.objects.values('create_at', 'status', 'name').annotate(count=Count('id')).order_by('-create_at')
    page = request.GET.get('page', 1)
    paginate_page = get_paginate(page, get_type, 10)
    
    #print(get_type)
    context = {
        'paginator' : paginate_page,
        'camers': get_camers,
        'types': get_type
    }
    return render(request, "index.html", context)

