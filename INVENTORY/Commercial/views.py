from django.shortcuts import render

# Create your views here.
def supplier(request):
    return render(request, 'list_supplier.html', {})