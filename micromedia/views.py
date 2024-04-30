from django.shortcuts import render

# Create your views here.
def elearn(request, *args, **kwargs):
    
    return render(request, 'index.html')
 