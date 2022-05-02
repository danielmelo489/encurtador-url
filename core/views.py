from django.shortcuts import render, redirect
import uuid
from .models import UrlCurta

def index(request):
    return render(request,'core/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        nova_url = UrlCurta(urlOriginal=link, urlEncurtada=uid)
        nova_url.save()
        context = {'url': uid}
    return render(request, 'core/detail.html', context)

def go(request, slug):
    url_original = UrlCurta.objects.get(urlEncurtada=slug).urlOriginal
    return redirect(url_original)
