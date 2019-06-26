from django.shortcuts import render
import os
# Create your views here.

from django.http import HttpResponse



def index(request):
    path = "ebdjango/static"
    img_list = os.listdir(path)
    return render(request, 'ecard/index.html', {'images': img_list})


