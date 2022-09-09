from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Articles, Comment
from .forms import create_article_form, edit_article_form, comment_form
from .registerform import register_form
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Articles.objects.all().order_by('-last_update')
    content = {'articles':articles}
    return render(request, 'index.html', content)

def view_article(request,a_id):
    article = Articles.objects.get(id=a_id)
    comments = article.comments.all().order_by('comment_date')
    form = comment_form()
    content = {'article':article, 'comments':comments, 'form':form}
    return render(request, 'view_article.html', content)

@login_required()
def create_article(request):
    if request.method == 'POST':
        Articles.objects.create(user=request.user,title=request.POST['title'],content=request.POST['content'],type=request.POST['type'])
        return redirect('index')
    else:
        form = create_article_form()
        content = {'form':form}
        return render(request, 'create_article.html', content)

@login_required()
def edit_article(request,a_id):
    if request.user == Articles.objects.get(id=a_id).user:
        if request.method == 'POST':
            Articles.objects.filter(id=a_id).update(title=request.POST['title'],content=request.POST['content'],type=request.POST['type'])
            return redirect('index')
        else:
            form = edit_article_form(a_id)
            content = {'form':form, 'a_id':a_id}
            return render(request, 'edit_article.html', content)
    else:
        content = {'content':'你不是這篇貼文的擁有者，不能修改內容哦!!!'}
        return render(request, 'fail.html', content)

@login_required()
def delete_article(request,a_id):
    if request.user == Articles.objects.get(id=a_id).user:
        Articles.objects.filter(id=a_id).delete()
        return redirect('index')
    else:
        content = {'content':'你不是這篇貼文的擁有者，不能刪除貼文哦!!!'}
        return render(request, 'fail.html', content)

#登入系統
def login(request):
    user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        return render(request, 'login_fail.html')

def signup(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(request,username=new_user.username,password=request.POST['password1'])
            auth_login(request, user)
            return redirect('index')
        else:
            content = {'form':form}
            return render(request, 'signup.html', content)
    else:
        form = register_form()
        content = {'form':form}
        return render(request, 'signup.html', content)

@login_required()
def new_comment(request,a_id):
    if request.method == 'POST':
        article = Articles.objects.get(id=a_id)
        Comment.objects.create(article=article,comment_user=request.user,comment_content=request.POST['comment_content'])
        return HttpResponseRedirect(reverse('view_article', kwargs={'a_id':a_id}))
    else:
        return redirect('index')

@login_required()
def edit_comment(request,a_id,c_id):
    if request.user == Comment.objects.get(id=c_id).comment_user:
        if request.method == 'POST':
            Comment.objects.filter(id=c_id).update(comment_content=request.POST['comment_content'])
            return HttpResponseRedirect(reverse('view_article', kwargs={'a_id':a_id}))
        else:
            comment = Comment.objects.get(id=c_id)
            form = comment_form()
            content = {'comment':comment, 'form':form, 'a_id':a_id}
            return render(request, 'edit_comment.html', content)
    else:
        content = {'content':'你不是這則留言的擁有者，不能修改內容哦!!!'}
        return render(request, 'fail.html', content)

@login_required()
def del_comment(request,a_id,c_id):
    if request.user == Comment.objects.get(id=c_id).comment_user:
        Comment.objects.filter(id=c_id).delete()
        return HttpResponseRedirect(reverse('view_article', kwargs={'a_id':a_id}))
    else:
        content = {'content':'你不是這則留言的擁有者，不能刪除留言哦!!!'}
        return render(request, 'fail.html', content)