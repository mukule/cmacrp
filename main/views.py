from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    business = Business.objects.all()  # Retrieve all companies from the database
    return render(request, 'main/index.html', {'business': business})

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')

# views.py
@login_required
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

def business(request, business_id):
    # Retrieve the Business object with the given primary key
    business = get_object_or_404(Business, pk=business_id)

    # Retrieve all companies associated with the business
    companies = Company.objects.filter(business=business)

    # You can add any additional context data you need for the detail view
    context = {
        'business': business,
        'companies': companies,  # Pass the list of companies to the template
    }

    return render(request, 'main/business.html', context)
@login_required
def edit_business(request, business_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            messages.success(request, 'Business updated successfully.')
            return redirect('main:create_business')  # Redirect to the business list view
    else:
        form = BusinessForm(instance=business)

    return render(request, 'main/edit_business.html', {'form': form, 'business': business})

@login_required
def delete_business(request, business_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

   
    business.delete()
    messages.success(request, 'Business deleted successfully.')
    return redirect('main:create_business')
@login_required
def create_company(request, business_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

    # Retrieve a list of companies within the selected business
    companies = Company.objects.filter(business=business)

    if request.method == 'POST':
        # Populate the initial 'business' field with the selected business
        form = CompanyForm(request.POST, initial={'business': business.id})
        if form.is_valid():
            form.save()
            messages.success(request, 'Company created successfully.')
            return redirect('main:create_company', business_id=business_id)  # Redirect to a company list view within the same business
    else:
        # Populate the form's 'business' field with the selected business (for display purposes)
        form = CompanyForm(initial={'business': business.id})

    return render(request, 'main/create_company.html', {'form': form, 'business': business, 'companies': companies})


@login_required
def edit_company(request, business_id, company_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

    # Retrieve the specific company within the selected business based on company_id
    company = get_object_or_404(Company, pk=company_id, business=business)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company updated successfully.')
            return redirect('main:create_company', business_id=business_id)  # Redirect to a company list view within the same business
    else:
        form = CompanyForm(instance=company)

    return render(request, 'main/edit_company.html', {'form': form, 'business': business, 'company': company})
@login_required
def delete_company(request, business_id, company_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

    # Retrieve the specific company within the selected business based on company_id
    company = get_object_or_404(Company, pk=company_id, business=business)

   
     # Delete the company
    company.delete()
    messages.success(request, 'Company deleted successfully.')
    return redirect('main:create_company', business_id=business_id)  # Redirect to a company list view within the same business

@login_required
def create_document(request, business_id, company_id):
    business = get_object_or_404(Business, pk=business_id)
    company = get_object_or_404(Company, pk=company_id, business=business)
    documents = Document.objects.filter(company=company)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, initial={'company': company})

        if form.is_valid():
            # Handle multiple file uploads
            files = request.FILES.getlist('file')  # Get a list of uploaded files
            for file in files:
                Document.objects.create(company=company, file=file)

            messages.success(request, 'Documents created successfully.')
            return redirect('main:create_document', business_id=business_id, company_id=company_id)

        else:
            messages.error(request, 'Error creating the documents. Please check the form.')

    else:
        form = DocumentForm(initial={'company': company})

    return render(request, 'main/create_docs.html', {'form': form, 'business': business, 'company': company, 'documents': documents})
@login_required
def delete_document(request, document_id):
    # Get the document object to delete
    document = get_object_or_404(Document, pk=document_id)

  
    # Delete the document
    document.delete()
    messages.success(request, 'Document deleted successfully.')

    # Redirect back to the document list or wherever you want
    return redirect('main:create_document', business_id=document.company.business.id, company_id=document.company.id)


def company(request, business_id, company_id):
    # Retrieve the specific business based on the provided business_id
    business = get_object_or_404(Business, pk=business_id)

    # Retrieve the specific company within the selected business based on company_id
    company = get_object_or_404(Company, pk=company_id, business=business)

    # Retrieve all documents related to the company
    documents = Document.objects.filter(company=company)

    # You can add any additional context data you need for the company detail view
    context = {
        'business': business,
        'company': company,
        'documents': documents,
    }

    return render(request, 'main/company.html', context)