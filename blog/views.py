from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import feedBackForm
from django.http import HttpResponse

# Create your views here.

def post_index(request):
  return render(request, 'post/index.html', {})


def post_list(request):
    object_list = Post.published.all()

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/list.html', {'page': page,
                                                   'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    return render(request, 'post/detail.html', {'post': post})

def feedback(request):
  if request.method != 'POST':
    form = feedBackForm()
  else:
    form = feedBackForm(request.POST,request.FILES or None)
    if form.is_valid():
      form.save()
  return HttpResponse('ok')