from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages

def index(request):
    business = Business.objects.all()  # Retrieve all companies from the database
    return render(request, 'main/index.html', {'business': business})


def dashboard(request):
    return render(request, 'main/dashboard.html')

# views.py

def create_business(request):
    businesses = Business.objects.all()  # Retrieve all businesses
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Business created successfully.')
            return redirect('main:create_business')  # Redirect to the same view
    else:
        form = BusinessForm()
    return render(request, 'main/create_business.html', {'form': form, 'businesses': businesses})

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company created successfully.')
            return redirect('main:create_company')  # Redirect to a company list view
    else:
        form = CompanyForm()
    return render(request, 'main/create_company.html', {'form': form})

def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document created successfully.')
            return redirect('document-list')  # Redirect to a document list view
    else:
        form = DocumentForm()
    return render(request, 'create_document.html', {'form': form})
