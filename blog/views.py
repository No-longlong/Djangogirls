from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
# render는 장고가 지원해주는 템플릿

def post_list(request): # 뷰(함수)에서 준비해서, 템블릿에 넘기는(return) 코드
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now()) # 현재시간보다 같거나 작은
    qs = qs.order_by('published_date') 
    
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })