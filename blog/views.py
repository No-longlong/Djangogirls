from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
# render는 장고가 지원해주는 템플릿

def post_list(request): # 뷰(함수)에서 준비해서, 템블릿에 넘기는(return) 코드
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now()) # 현재시간보다 같거나 작은
    qs = qs.order_by('published_date') 
    
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # 아래의 것들과 똑같은 기능
    # pk = "100"
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404 #page not found
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

def post_new(request):
    # request.Post, request.FILES 데이터가 담기는곳인데, 
    # 이것을 처리하는 로직이 없기 때문에 '게시'눌러도 빈폼만 나타나는 현상

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # 비로그인자는 글 올리면 에러
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # 비로그인자는 글 올리면 에러
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form
    })