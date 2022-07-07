
from django.urls import path

from myapp.views import form_view
 
urlpatterns = [
    path('', form_view)
    
]