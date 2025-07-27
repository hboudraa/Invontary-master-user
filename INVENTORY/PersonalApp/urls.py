from django.urls import path
from . import views

app_name = 'personal'  # Namespace for this app's URLs

urlpatterns = [
    path('Requisitionner/', views.requisition, name='requisition'),
    path('utilisateur/', views.utilisateur, name='utilisateur'),
    path('charger/', views.charger, name='charger'),
    path('delegue/', views.delegue, name='delegue'),
    path('sg/', views.sg, name='sg'),
]
