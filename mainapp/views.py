from django.shortcuts import render

from mainapp.models import carousel, man, about
from post.models import post2
from kurs.models import Course

def index(request):
    carouse = carousel.objects.all()[:6]
    kurs1 = Course.objects.all()
    men = man.objects.all()
    post = post2.objects.all()[:3]
    dataAll = {
        'corusel': carouse,
        'kurs': kurs1,
        'man': men,
        'post': post
    }
    return render(request, 'home/index.html', {'dataAll': dataAll})

def info(request):
    info1 = about.objects.all()[:1]
    data = {
        'io': info1

    }
    return render(request, 'home/about.html', {'data': data})
def contact(request):
    return render(request, 'home/contact.html')
