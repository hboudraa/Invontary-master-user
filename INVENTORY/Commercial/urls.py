from django.urls import path
from . import views

app_name = 'commercial'  # Namespace for this app's URLs

urlpatterns = [
    path('supplier/', views.supplier, name='supplier'),
]