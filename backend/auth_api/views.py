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
            future = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            payload = {
                'user_id': this_user.pk,
                'exp': calendar.timegm(future.timetuple())
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            response = {'token': token}
            return JsonResponse(response, safe=False)
        else:
            response = {'error': 'user is not active'}
            return JsonResponse(response, safe=False)
    else:
        response = {'error': 'user is not found'}
        return JsonResponse(response, safe=False)

@csrf_exempt
def get_user_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    token = body['token']

    try:
        jwt_data = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(jwt_data)
        user_data = User.objects.get(pk = jwt_data['user_id'])
        response = {
            'email': user_data.email,
            'username': user_data.username,
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
        }
        return JsonResponse(response, safe=False)
    except jwt.ExpiredSignatureError:
        response = {
            'error': 'token is expired!',
        }
        return JsonResponse(response, safe=False)
    except jwt.exceptions.DecodeError:
        response = {
            'error': 'token is invalid!'
        }
        return JsonResponse(response, safe=False)
