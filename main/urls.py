from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_business/", views.create_business, name="create_business"),
    path("create_company/", views.create_company, name="create_company"),
    path("create_document/", views.create_document, name="create_document"),
    
]