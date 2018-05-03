from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.

@csrf_exempt
def auth_view(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = authenticate(username=body['login'], password=body['password'])
    if user is not None:
        if user.is_active:
            this_user = User.objects.get(username = body['login'])
            result = {'id': this_user.pk,'username': this_user.username, 'first_name': this_user.first_name, 'last_name': this_user.last_name }
            return JsonResponse(result, safe=False)
        else:
            result = {'error': 'user is not active'}
            return JsonResponse(result, safe=False)
    else:
        result = {'error': 'user is not found'}
        return JsonResponse(result, safe=False)
