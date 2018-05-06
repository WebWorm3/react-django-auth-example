from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, jwt, random, string, datetime, calendar



@csrf_exempt
def auth_view(request):

    # def random_char(y):
    #    return ''.join(random.choice(string.ascii_letters) for x in range(y))

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    user = authenticate(username=body['login'], password=body['password'])
    if user is not None:
        if user.is_active:
            this_user = User.objects.get(username = body['login'])
            # random_word = random_char(8)
            future = datetime.datetime.utcnow()
            payload = {
                'user_id': this_user.pk,
                'exp': future
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            result = {'username': this_user.username, 'token': token}
            return JsonResponse(result, safe=False)
        else:
            result = {'error': 'user is not active'}
            return JsonResponse(result, safe=False)
    else:
        result = {'error': 'user is not found'}
        return JsonResponse(result, safe=False)

# @csrf_exempt
# def get_user_data(request):
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#
#     token = body['token']
#     user = body['user']
