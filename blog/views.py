from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# READ
def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

# DETAIL READ
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


# CREATE
def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.image = request.FILES.get('image')
    new_blog.save()
    return redirect('detail', new_blog.id)  #-> redirect가 post를 get으로 바꿔준다. render 쓰면 post요청이 get요청으로 바뀌지 않아 새로고침할 경우 post 요청이 계속 생김. 이게 돈 인출일 경우 계속 돈 인출 되는 것
    # return render(request, 'detail.html', {'blog': new_blog})



# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog})


# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')