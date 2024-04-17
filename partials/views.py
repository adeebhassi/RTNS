from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
<<<<<<< HEAD
def HeaderFooterView(request):
    try:
        header_data=WebsiteHeader.objects.get()
        footer_data=WebsiteFooter.objects.get()
        dep_logo=DepartmentLogo.objects.all()
=======
def HeaderView(request):
    try:
        header_data=WebsiteHeader.objects.get()
>>>>>>> 1406f061cf995df5ec610e3f42e15e668e41998a
    except ObjectDoesNotExist:
        header_data=None
        
    print("head is",header_data)
<<<<<<< HEAD
    print("foo",footer_data)
    content={
        'header':header_data,
        'footer':footer_data,
        'dep_logos':dep_logo
=======
    content={
        'header':header_data
>>>>>>> 1406f061cf995df5ec610e3f42e15e668e41998a
    }  
    return render(request,'partials/base.html',content)
        
