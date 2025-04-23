from django.urls import path
from . import views

app_name = 'product'  # Namespace for this app's URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('export/excel/', views.export_products_to_excel, name='export_products_to_excel'),
    path('add-product/', views.add_product, name='add-product'),

    path('AddStockEnter/<int:id>/', views.add_enter, name='AddStockEnter'),
    path('fiche-stock-entr/<int:pk>', views.fiche_stock_entr, name='fiche_stock_entr'),

    path('AddStockSortie/<int:id>/', views.add_sortie, name='AddStockSortie'),
    path('fiche-stock-sort/<int:pk>', views.fiche_stock_sortie, name='fiche_stock_sort'),

    path('demander/<int:id>/', views.demand, name='demander'),
    path('demand/<int:demand_id>/<str:status>/', views.update_demand_status, name='update_demand_status'),
    path('all-demands/', views.all_demands, name='all_demands'),
]


