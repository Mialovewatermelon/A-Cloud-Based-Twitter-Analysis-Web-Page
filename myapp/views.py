# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response={}
    try:
        book = request.GET.get('book_name')
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
# 给piechart提供每一部分的数据 格式为[{value: , name;''}]
def get_geodata(request):
    response={}
    try:
        response['msg']='Success'
        response['pieChartData'] = [
        { 'value': 10, 'name': '山东' },
        { 'value': 55, 'name': '北京' },
        { 'value': 45, 'name': '云南' }]
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)