from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import json


def index(request):
    return render(request, 'index.html')

@require_http_methods(["GET"])
# 给piechart提供每一部分的数据 格式为[{value: , name;''}]
def get_geodata(request):
    response={}
    try:
        response['msg']='Success'
        response['pieChartData'] = [
        { 'value': 10, 'name': 'shandong' },
        { 'value': 55, 'name': 'beijing' },
        { 'value': 45, 'name': 'yunnan' }]
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)