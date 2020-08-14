from django.shortcuts import render

# Create your views here.
# render는 장고가 지원해주는 템플릿
def post_list(request):
    return render(request, 'blog/post_list.html')