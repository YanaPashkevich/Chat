from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import os
import time
import json

from django.http.response import JsonResponse
from django.contrib.auth import get_user_model


from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from pusher import Pusher


pusher_client = Pusher (app_id='1482662',
                       key='9ecd2e32593d282a3cd7',
                       secret='10a45ff84f07189496e5',
                       ssl=False,
                       cluster='eu')
                       


@login_required(login_url='/main/')
def video(request):
    User = get_user_model()
    all_users = User.objects.exclude(id=request.user.id).only('id', 'username')
    return render(request, 'video.html', {'allUsers': all_users})


def pusher_auth(request):
    payload = pusher_client.authenticate(
        channel=request.POST['channel_name'],
        socket_id=request.POST['socket_id'],
        custom_data={
            'user_id': request.user.id,
            'user_info': {
                'id': request.user.id,
                'name': request.user.username
            }
        })
    return JsonResponse(payload)


def generate_agora_token(request):
    appID = os.environ.get('17268e6e3f314edbb58da6fb080d4c82')
    appCertificate = os.environ.get('23dd1f6e1c80423b9195e6a6216e6678')
    channelName = json.loads(request.body.decode(
        'utf-8'))['channelName']
    userAccount = request.user.username
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    token = RtcTokenBuilder.buildTokenWithAccount(
        appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    return JsonResponse({'token': token, 'appID': appID})


def call_user(request):
    body = json.loads(request.body.decode('utf-8'))

    user_to_call = body['user_to_call']
    channel_name = body['channel_name']
    caller = request.user.id

    pusher_client.trigger(
        'presence-online-channel',
        'make-agora-call',
        {
            'userToCall': user_to_call,
            'channelName': channel_name,
            'from': caller
        }
    )
    return JsonResponse({'message': 'call has been placed'})

