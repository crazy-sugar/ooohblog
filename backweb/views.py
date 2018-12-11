from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.artform import AddArtForm, EditArtForm
from backweb.models import Article
from backweb.userform import RegistrationForm, LoginForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect('/backweb/login/')
        else:
            return HttpResponse('sorry,you can not register')
    else:
        user_form = RegistrationForm()
        return render(request,'backweb/register.html',{'form':user_form})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect('/backweb/my_index/')
            else:
                err = '用户名或密码错误'
                return render(request, 'backweb/login.html', {'err': err})


def my_index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'backweb/article.html',{'articles':articles})


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        articles = Article.objects.all()
        paginator = Paginator(articles,2)
        page = paginator.page(page)
        return render(request,'backweb/article.html',{'page':page})


def add_article(request):
    if request.method == 'GET':
        return render(request,'backweb/add_article.html')

    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            keywords = form.cleaned_data['keywords']
            Article.objects.create(title=title, desc=desc,
                                   content=content, icon=icon,
                                   keywords=keywords)
            return render(request,'backweb/article.html')
        else:
            errors = form.errors
            return render(request, 'backweb/add_article.html', {'errors': errors})


def article_list(request):
    if request.method == 'GET':

        return render(request,'backweb/art.html')


def del_article(request, id):
    # 推荐传参通过此种方法
    # 页面展示a标签href为{% url 'art:del_art_id' art.id %}
    # 如果id=3,表示跳转{/article/del_art_id/3/}
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def edit_article(request,id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request,'backweb/edit_article.html',{'article':article})

    if request.method == 'POST':
        form = EditArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add_article.html', {'form': form, 'article': article})













