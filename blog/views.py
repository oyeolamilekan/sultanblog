#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post,Ads,Profile,Mentee
from .forms import feedBackForm,AskJolaForm
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def post_index(request):
  ad = Ads.objects.order_by('?')[0:1]
  return render(request, 'post/index.html', {'ads':ad})


def post_list(request):
    ad = Ads.objects.order_by('?')[0:1]
    object_list = Post.published.all()
    profile = Profile.objects.get(owner_status='owner')
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
                                                   'posts': posts,'ads':ad,'profile':profile})

def post_detail(request, year, month, day, post):
    ad = Ads.objects.order_by('?')[0:1]
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    if request.method == 'GET':
      post.page_views += 1
      post.save()
    return render(request, 'post/detail.html', {'post': post,'ads':ad})

def feedback(request):
    if request.method != 'POST':
      form = feedBackForm()
    else:
      form = feedBackForm(request.POST,request.FILES or None)
      if form.is_valid():
        form.save()
    return HttpResponse('ok')

def askjola(request):
    if request.method != 'POST':
      form = AskJolaForm()
    else:
      form = AskJolaForm(request.POST,request.FILES or None)
      if form.is_valid():
        form.save()
    return HttpResponse('ok')

    #send_mail(subject,message,from_email,reciever_list,fail_silently=False,html_message=html_message)

