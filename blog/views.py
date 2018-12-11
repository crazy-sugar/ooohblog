from django.shortcuts import render

# Create your views here.
from backweb.models import Article


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'blog/index.html',{'articles':articles})


