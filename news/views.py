from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .models import News, Category
from .utils import MyMixin
from django.core.mail import send_mail
from Dev import settings


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        categories = Category.objects.all()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы зарегистрировались.')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка')
    else:
        form = UserRegisterForm()
        categories = Category.objects.all()

    return render(request, 'news/register.html', {'form': form, 'categories': categories})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form, })


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        categories = Category.objects.all()
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['content']
            email_from = settings.EMAIL_HOST_USER
            recipient = ['era.ab.02@gmail.com', ]
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'era.ab.02@gmail.com',
                             ['era.ab.02@gmail.com', 'sakenab11@gmail.com', ], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено.')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки письма')

            return redirect('home')
    else:
        form = ContactForm()
        categories = Category.objects.all()
    return render(request, 'news/test.html', {'form': form, 'categories': categories})


class HomeNews(ListView, MyMixin):
    paginate_by = 2
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    mixin_prop = 'hello world'

    def get_queryset(self):
        return News.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['categories'] = Category.objects.all()
        context['mixin'] = self.get_prop()
        return context


class CategoryList(ListView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = Category.objects.get(pk=self.kwargs['pk'])
        return context


class DetailNews(DetailView):
    model = News
    context_object_name = 'news_item'

    # pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super(DetailNews, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreatNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CreatNews, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
