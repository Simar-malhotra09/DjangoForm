from django.shortcuts import render

from django.http import JsonResponse

 
# Create your views here.
def form_view(request):
    data= {
             
                    "name": "Manish Verma",
                    "username": "mandrake",
                    "email": "manish@drake.co.in",
                    "mobile": "8054978283",
                    "password": "12345678",
                    "code": "AAX09Z",
                    }

            
        
    
    
    
    context={ 'data': data}
    return render(request, "form.html", context)
    
   
