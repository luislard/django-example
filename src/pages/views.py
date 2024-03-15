from django.shortcuts import render
from .models import Blog

# Create your views here.
def about(request):
   return render(request, 'about.html')


# Create your views here.
def home(request):
   pages = Blog.objects.all().order_by('-created_at')
   context = {
      'title': 'Lista de Paginas',
      'items': pages[:3]
   }
   return render(request, 'home.html', context)
