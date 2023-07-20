from django.shortcuts import render

# Create your views here.
from app.models import Posts

def home(request):
    context= {
        'posts':Posts.objects.all()
    }
    return render(request, 'index.html', context=context)