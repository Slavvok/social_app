from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
import requests
import random

def index(request):
    if request.user.is_authenticated:
        return redirect('/info/')
    else:
        return render(request, "index.html")


def get_info(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    url = 'https://api.vk.com/method/friends.get'
    social = request.user.social_auth.get(provider='vk-oauth2')
    token = social.extra_data['access_token']
    number = int(request.GET.get("friends", "5"))
    if token:
        data = {'access_token': token,
                'v': '5.92',
                'fields': 'nickname, photo_50'}
        r = requests.get(url, data)
        info = random.sample(r.json()['response']['items'], k=number)
        context = {'info': info}
    return render(request, 'info.html', context, )


<<<<<<< HEAD
def handler404(request):
    respnse = render(request, '404.html')
    response.status = 404
    return response
=======
def handler404(request, *args, **kwargs):
    response = render_to_response("404.html")
    response.status_code = 404
    return reponse
>>>>>>> 01d4c024dddf9375ac7ccc3c3b76d69333713388


def logout(request):
    auth_logout(request)
