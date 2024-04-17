from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def HeaderFooterView(request):
    try:
        header_data=WebsiteHeader.objects.get()
        footer_data=WebsiteFooter.objects.get()
        dep_logo=DepartmentLogo.objects.all()
    except ObjectDoesNotExist:
        header_data=None
        
    print("head is",header_data)
    print("foo",footer_data)
    content={
        'header':header_data,
        'footer':footer_data,
        'dep_logos':dep_logo
    }  
    return render(request,'partials/base.html',content)
        
