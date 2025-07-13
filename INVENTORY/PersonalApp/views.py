from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Charger

# Create your views here.

def utilisateur(request):
    return render(request, 'utilisateur.html', {})

@staff_member_required
def charger(request):
    list_charge = Charger.objects.all()
    paginator = Paginator(list_charge, 26)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'charger.html', {
        'page_obj': page_obj
    })

def delegue(request):
    return render(request, 'delegue.html', {})

def sg(request):
    return render(request, 'sg.html', {})

def requisition(request):
    return render(request, 'Réquisitionner.html', {})
