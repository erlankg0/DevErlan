from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm
from .models import News, Category
from .utils import MyMixin


def test(request):
    objects = ['Erlan', 'Daniel', 'Saken', 'Ozcan', 'Ozan', 'Onan', 'Askar', 'Rasul', 'Daniyar', 'Kani', 'Kayrat']
    paginator = Paginator(objects, 3)
    pag_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(pag_num)
    return render(request, 'news/test.html', {'page_obj': page_obj, 'object': objects})


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
