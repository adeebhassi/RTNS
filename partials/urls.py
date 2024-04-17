from django.urls import path
from .views import *


app_name="partials"

urlpatterns=[
<<<<<<< HEAD
    path("header",HeaderFooterView,name="header"),
=======
    path("header",HeaderView,name="header"),
>>>>>>> 1406f061cf995df5ec610e3f42e15e668e41998a
    # path('ajax/load-subarea/',load_subarea, name='ajax_load_subarea'),
    
]