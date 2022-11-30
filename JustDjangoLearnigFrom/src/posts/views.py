from django.db.models import Count
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, render
from marketing.forms import SignupForm
from django.urls import reverse
from . models import Author, Post, Tages


def get_tags():
    tages = Tages.objects.all()
    return tages


def get_category_count():
    queryset = Post.objects.values(
        'categories__title').annotate(Count('categories__title'))
    return queryset


def index(request):
    queryset = Post.objects.filter(featured=True)[:3]
    latest_post = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = SignupForm(request.POST)
        if email.is_valid():
            email.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        email = SignupForm()

    context = {
        'object_list': queryset,
        'latest_post': latest_post,
        'form': email
    }
    return render(request, 'index.html', context)


def blog(request):
    tages = get_tags()
    category_count = get_category_count()
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    latest_post = Post.objects.order_by('timestamp')

    context = {
        'latest_post': latest_post,
        'page_obj': page_obj,
        'category_count': category_count,
        'tages': tages

    }
    return render(request, 'blog.html', context)


def post(request, pk):
    return render(request, 'post.html')
