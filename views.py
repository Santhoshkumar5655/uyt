import json
from django.http import HttpRequest, JsonResponse
from .models import School
from django.db.models import Avg

def classAvgheightView(request: HttpRequest):
    json_response = {}
    for i in  School.objects.all().values_list("_class").annotate(Avg('height')):
        json_response[i[0]] = i[1]
    return JsonResponse(json_response)

def classAvgGenderHeightView(request: HttpRequest):
    json_response = {}
    for i in  School.objects.all().values("_class", "gender").annotate(Avg('height')):
        
        if json_response.get(i["_class"], None) is None:
            json_response[i["_class"]] = {}
        
        if i['gender'] == "M":
            json_response[i["_class"]]['M'] = i['height__avg']
        else:
            json_response[i["_class"]]['F'] = i['height__avg']
    return JsonResponse(json_response)

def classRegInFeb(request: HttpRequest):
    json_response = {}
    for i in  School.objects.filter(month = 2).order_by("day"):
        if i._class in json_response.keys():
            json_response[i._class] += 1
        else:
            json_response[i._class] = 1
    return JsonResponse(json_response)


def classSecAvgHeiWei(BaseView):
    json_response = []
    for i in School.objects.all().values("_class", "section").annotate(Avg('height'), Avg('weight')):
        temp = {}
        temp["_class"] = i["_class"]
        temp['section'] = i["section"]
        temp['height'] = i["height__avg"]
        temp['weight'] = i["weight__avg"]
        json_response.append(temp)
    return JsonResponse(json_response, safe = False)