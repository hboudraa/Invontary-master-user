from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Charger, Utilisateur, SG
from django.shortcuts import render

# Create your views here.
@staff_member_required
def utilisateur(request):
    list_users = Utilisateur.objects.all()
    paginator = Paginator(list_users, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'utilisateur.html', {
        'page_obj': page_obj
    })

@staff_member_required
def charger(request):
    list_charge = Charger.objects.all()
    paginator = Paginator(list_charge, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'charger.html', {
        'page_obj': page_obj
    })

def delegue(request):
    return render(request, 'delegue.html', {})

def sg(request):
    list_sg = SG.objects.all()
    paginator = Paginator(list_sg, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'sg.html', {
        'page_obj': page_obj
    })

def requisition(request):
    return render(request, 'Réquisitionner.html', {})
