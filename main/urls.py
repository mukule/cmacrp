from django.urls import path
from . import views



app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_business/", views.create_business, name="create_business"),
    path("create_company/<int:business_id>/", views.create_company, name="create_company"),
    path("create_document/<int:business_id>/<int:company_id>/", views.create_document, name="create_document"),
    path('business/<int:business_id>/', views.business, name='business'),
    path('edit_business/<int:business_id>/', views.edit_business, name='edit_business'),
    path('edit_company/<int:business_id>/<int:company_id>/', views.edit_company, name='edit_company'),
    path('delete_business/<int:business_id>/', views.delete_business, name='delete_business'),
    path('delete_company/<int:business_id>/<int:company_id>/', views.delete_company, name='delete_company'),
    path('company/<int:business_id>/company/<int:company_id>/', views.company, name='company'),
    path('delete_document/<int:document_id>/', views.delete_document, name='delete_document'),

    
]