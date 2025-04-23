import openpyxl
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import ProductForm, EnterForm, DemandClassForm, SortieForm
from .models import *
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def products(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        product_list = Product.objects.filter(category_id=selected_category)
    else:
        product_list = Product.objects.all().order_by('id')
    search_query = request.GET.get('search_query', '')
    if search_query:
        product_list = product_list.filter(name__icontains=search_query)
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Handle AJAX request for live search
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('product_list.html', {'page_obj': page_obj})
        return JsonResponse({'html': html})
    return render(request, 'list_products.html',
                  {
                      'categories': categories,
                      "page_obj": page_obj,
                      'selected_category': selected_category
                  })

def add_enter(request, id):
    enter = Product.objects.get(pk=id)  # ✅ جلب كائن المنتج الصحيح
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_enter = EnterForm(request.POST, product=enter)  # ✅ تمرير كائن المنتج للنموذج
            if form_enter.is_valid():
                fiche_enter = form_enter.save(commit=False)
                fiche_enter.user = request.user
                fiche_enter.name_fiche = enter  # ✅ تعيين كائن المنتج بدلاً من اسمه
                fiche_enter.save()
                messages.success(request, "✅ Fiche added successfully!")
                return redirect('product:AddStockEnter', id=id)
            else:
                print(form_enter.errors)  # عرض الأخطاء في الكونسول
                messages.error(request, "❌ Error: Please check the form fields.")
        else:
            form_enter = EnterForm(product=enter)  # ✅ تمرير المنتج عند تحميل الصفحة لأول مرة
        return render(request, 'AddStockEnter.html', {'form_enter': form_enter})
    messages.error(request, "❌ You must be logged in to add a product.")
    return redirect('accounts:login')  # توجيه المستخدم إلى صفحة تسجيل الدخول


def fiche_stock_entr(request, pk):
    item = get_object_or_404(Product, pk=pk)
    list_fiche = FicheStockEntr.objects.filter(name_fiche=item).order_by('id')  # 🔹 تصفية السجلات للمنتج المحدد
    paginator = Paginator(list_fiche, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'ficheStockEntr.html', {
        'item': item,
        "page_obj": page_obj
        })


def add_sortie(request, id):
    sortie = Product.objects.get(pk=id)
    ini_quantity = sortie.quantity
    print(ini_quantity)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_sortie = SortieForm(request.POST, product=sortie)
            if form_sortie.is_valid():
                fiche_sortie = form_sortie.save(commit=False)
                fiche_sortie.user = request.user
                fiche_sortie.name_fiche = sortie
                if form_sortie.cleaned_data['quantity'] <= ini_quantity:
                    fiche_sortie.save()
                    messages.success(request, "✅ Fiche added successfully!")
                    return redirect('product:fiche_stock_sort', pk=id)
                else:
                    messages.error(request, '❌ Error: Please check the QUANTITY form fields.')
            else:
                print(form_sortie.errors)
                messages.error(request,"❌ Error: Please check the form fields.")
        else:
            form_sortie = SortieForm(product=sortie)
        return render(request, 'add-stock-sortie.html', {'form_sortie':form_sortie})
    messages.error(request, "❌ You must be logged in to add a product.")
    return redirect('accounts:login')  # توجيه المستخدم إلى صفحة تسجيل الدخول

def fiche_stock_sortie(request, pk):
    item = get_object_or_404(Product, pk=pk)
    list_fiche = FicheStockSortie.objects.filter(name_fiche=item).order_by('id')  # 🔹 تصفية السجلات للمنتج المحدد
    paginator = Paginator(list_fiche, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'ficheStockSort.html', {
        'item': item,
        "page_obj": page_obj
    })

def demand(request, id):
    product = get_object_or_404(Product, pk=id)

    if not request.user.is_authenticated:
        messages.error(request, "❌ You must be logged in to add a product.")
        return redirect('accounts:login')

    if request.method == 'POST':
        form = DemandClassForm(request.POST, product=product)
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user
            demand.name_demand = product
            demand.save()
            messages.success(request, "✅ Demande added successfully!")
            return redirect('product:products')
        else:
            print(form.errors)
            messages.error(request, "❌ Error: Please check the form fields.")
    else:
        form = DemandClassForm(product=product)
    if request.user.is_superuser:
        list_demand = DemandClass.objects.filter(name_demand=product).order_by('id')
    else:
        list_demand = DemandClass.objects.filter(name_demand=product, user=request.user).order_by('id')
    paginator = Paginator(list_demand, 10)
    page_number = (request.GET.get("page"))
    page_obj = paginator.get_page(page_number)
    return render(request, 'demander.html', {
        'form_demand': form,
        'demand_id': product,
        'page_obj':page_obj,
    })

@staff_member_required
def all_demands(request):
    list_demand = DemandClass.objects.all().order_by('-date')
    paginator = Paginator(list_demand, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'all_demands.html', {
        'page_obj': page_obj
    })


@staff_member_required
def update_demand_status(request, demand_id, status):
    demand = get_object_or_404(DemandClass, pk=demand_id)

    if status in ['accepted', 'rejected']:
        demand.status = status
        demand.save()
        messages.success(request, f"✅ Demande {status} successfully.")
    else:
        messages.error(request, "❌ Invalid status.")

    return redirect(request.META.get('HTTP_REFERER', 'product:products'))
    

def add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                messages.success(request, "✅ Product added successfully!")
                return redirect('product:products')
            else:
                print(form.errors)  # Debugging: show errors in console
                messages.error(request, "❌ Error: Please check the form fields.")
        else:
            form = ProductForm()
        return render(request, 'add_product.html', {'form': form})

    # Redirect unauthenticated users
    messages.error(request, "❌ You must be logged in to add a product.")
    return redirect('accounts:login')  # Change 'login' to your actual login URL name



def export_products_to_excel(request):
    # Create a workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Products"

    # Define the column headers
    headers = ['ID', 'Name', 'Category', 'Quantity', 'Price']

    # Add headers to the worksheet
    ws.append(headers)

    # Fetch all products from the database
    products = Product.objects.all()

    # Add product data to the worksheet
    for product in products:
        ws.append(
            [product.id, product.name, product.category.name, product.quantity, product.price])

    # Prepare the response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'

    # Save the workbook to the response
    wb.save(response)

    return response
