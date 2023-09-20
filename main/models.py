from django.db import models
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage



class Business(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def document_upload_path(instance, filename):
    # instance.company.business.name contains the business name, and instance.company.name contains the company name
    return f'{instance.company.business.name}/{instance.company.name}/documents/{filename}'

def validate_pdf_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class PreserveExtensionStorage(FileSystemStorage):
    def get_valid_name(self, name):
        return name

# In your Document model
class Document(models.Model):
    # Use FileExtensionValidator to validate the file extension
    file = models.FileField(
        upload_to=document_upload_path,
        storage=PreserveExtensionStorage(),  # Use the custom storage
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name