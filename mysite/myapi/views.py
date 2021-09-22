# views.py
from rest_framework import viewsets
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .serializers import *
from .models import *
from .forms import *

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

import datetime

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('title')
    serializer_class = ImageSerializer   


def index(request):

    if request.method == 'GET':
        user = User.objects.filter(name = "User1").first()
        imgs = Image.objects.filter(owner = user)

        form = ImageForm()

        return render(request, "index.html", {'imgs': imgs, 'form': form}) 

    # google vision code
    else:
        user = User.objects.filter(name = "User1").first()
        # imgs = Image.objects.filter(owner = user)
        # call_type = request.POST.get('call_type')
        
        # get user image input
        img = request.FILES['image'].file.read()

        # use google vision api to get labels from image
        image = vision.Image(content=img)
        client = vision.ImageAnnotatorClient()
        response = client.label_detection(image=image)
        labels = response.label_annotations
        # print('Labels:')
        # for label in labels:
        #     print(label.description)

        # get images from databse that fit the labels    
        imgs = Image.objects.filter(title__icontains = labels[0].description)
        labels = labels[1:]
        for label in labels:
            print(label.description)
            imgs = imgs | Image.objects.filter(title__icontains = label.description)
        
        result = {}

        form = ImageForm()

        return render(request, "index.html", {'imgs': imgs, 'form': form}) 


def search(request):

    if request.method == 'GET':

        info = ""
        # info['html_for_img_gallery'] = object_.html_for_DTC_application()
        #tmp_info['html_for_opportunity_detail_page_edit_form_header'] = object.html_for_opportunity_detail_page_edit_form_header()
        #tmp_info['html_for_toast'] =
                

        search_input = request.GET.get("search_input")
        search_input_list = search_input.split(" ")
        print("search_input_list: ", search_input_list)
        imgs = Image.objects.filter(title__icontains = search_input_list[0])
        search_input_list = search_input_list[1:]
        for inp in search_input_list:
            print(inp)
            imgs = imgs | Image.objects.filter(title__icontains = inp)
        
        result = {}

        for img in imgs:
            info += img.html_for_img_gallery()

        result["info"] = info
        # return HttpResponse(200)  
        return JsonResponse(result)     

    else:
        search_input = request.GET.get("search_input")
        search_input_list = search_input.split(" ")
        print("search_input_list: ", search_input_list)
        imgs = Image.objects.filter(title__icontains = search_input_list[0])
        search_input_list = search_input_list[1:]
        for inp in search_input_list:
            print(inp)
            imgs = imgs | Image.objects.filter(title__icontains = inp)
        print(imgs)

        # return HttpResponse(200)
        return render(request, "index.html", {'imgs': imgs})    

       