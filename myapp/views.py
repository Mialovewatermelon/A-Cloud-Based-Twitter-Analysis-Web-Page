from django.shortcuts import render
import couchdb
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from myapp import couchdb_url
import json
import os

path = os.getcwd()

with open(path+'/myapp/analysis.json', encoding='utf-8') as f:
    output = json.load(f)
with open(path+'/myapp/china.json', encoding='utf-8') as f:
    china_output = json.load(f)
with open(path+'/myapp/age_distribution.json', encoding='utf-8') as f:
    age = json.load(f)
with open(path+'/myapp/election.json', encoding='utf-8') as f:
    election = json.load(f)

states = ['vic', 'nsw', 'southern', 'western', 'tas', 'queens']



def index(request):
    return render(request, 'index.html')

def get_view_data(DB, state, viewname, type='reduce'):
    if type == 'reduce':
        result = DB[state].view(viewname)
        if len(result) == 0:
            return 0
        else:
            return [row.value for row in result][0]
    if type == 'text':
        result = DB[state].view(viewname, limit=5)
        return [row.value for row in result]

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


@require_http_methods(["GET"])

def get_data(request):
    DB = couchdb.Server(couchdb_url.url)
    print(couchdb_url.url)
    for i in DB:
        print(i)
    response={}
    try:
        for state in states:
            if request.GET.get('state') == state:
                response['LabelData'] = [
                    {'name': 'positive',
                     'value': int(output['output_'+state]['pos']) + int(get_view_data(DB, state, 'tweeterData/pos'))},
                    {'name': 'negtive',
                     'value': int(output['output_' + state]['neg']) + int(get_view_data(DB, state, 'tweeterData/neg'))}
                    ]
                response['LabelData_China'] = [
                    {'name': 'China positive',
                     'value': int(china_output['output_'+state]['pos']) + get_view_data(DB, state, 'tweeterData/china_pos')},
                    {'name': 'China negtive',
                     'value': int(china_output['output_' + state]['neg']) + get_view_data(DB, state, 'tweeterData/china_neg')}
                    ]
                response['TextData_pos'] = [
                    get_view_data(DB,state,'tweeterData/pos_text',type='text')
                ]
                response['TextData_neg'] = [
                    get_view_data(DB,state,'tweeterData/neg_text',type='text')
                ]
                response['TextData_china_pos'] = [
                    get_view_data(DB, state, 'tweeterData/china_pos_text',type='text')
                ]
                response['TextData_china_neg'] = [
                    get_view_data(DB, state, 'tweeterData/china_neg_text',type='text')
                ]
                response['ageData'] = [
                    {'name': '0~14 years old', 'value': age[state]['persons_0_14_percentage']},
                    {'name': '15~64 years old', 'value': age[state]['persons_15_64_percentage']},
                    {'name': '65+ years old', 'value': age[state]["persons_65_plus_percentage"]}
                ]
                response['election'] = [
                    {'name': 'labor party', 'value': election[state]['australian_labor_party_votes']},
                    {'name': 'national coalition', 'value': election[state]["liberal_national_coalition_votes"]}
                ]
                response['msg']='Success'
                response['msg']=0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)