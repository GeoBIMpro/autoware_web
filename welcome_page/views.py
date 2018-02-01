# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'welcome_page/index.html')

#def development(request):
#    return render(request, 'welcome_page/development.html')

def join(request):
    return render(request, 'welcome_page/join.html')

def development(request):
    return render(request, 'welcome_page/development.html')

def development2(request):
    return render(request, 'welcome_page/development2.html')

def docker_x86_install(request):
    return redirect('https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86')
    # return render(request, 'welcome_page/docker_x86.html')

def docker_px2_install(request):
    # return render(request, 'welcome_page/docker_px2_tier4.html')
    return redirect('https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-DRIVE-PX2')

def sample_data1(request):
    return redirect('https://autoware.blob.core.windows.net/sample/sample_moriyama_data.tar.gz')

def sample_data2(request):
    return redirect('https://autoware.blob.core.windows.net/sample/my_launch.sh')

def sample_data3(request):
    return redirect('https://autoware.blob.core.windows.net/sample/sample_moriyama_150324.tar.gz')
