from django.shortcuts import render

# Create your views here.

def utilisateur(request):
    return render(request, 'utilisateur.html', {})

def charger(request):
    return render(request, 'charger.html', {})

def delegue(request):
    return render(request, 'delegue.html', {})

def sg(request):
    return render(request, 'sg.html', {})

def requisition(request):
    return render(request, 'Réquisitionner.html', {})
