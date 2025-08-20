from django.shortcuts import render, redirect
from .forms import SupplierForm
from .models import Supplier


# Create your views here.
def supplier(request):
    list_supplier = Supplier.objects.all()
    return render(request, 'list_supplier.html', {'list_supplier': list_supplier})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commercial:supplier')  # غيّرها للمكان المناسب
    else:
        form = SupplierForm()
    return render(request, 'add_supplier.html', {'form': form})