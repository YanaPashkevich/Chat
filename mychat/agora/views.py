# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# import os
# import time
# import json

# from django.http.response import JsonResponse
# from django.contrib.auth import get_user_model


# from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
# from pusher import Pusher


# pusher_client = Pusher (app_id='1482662',
#                        key='9ecd2e32593d282a3cd7',
#                        secret='10a45ff84f07189496e5',
#                        ssl=False,
#                        cluster='eu')
                       


# @login_required(login_url='/main/')
# def video(request):
#     User = get_user_model()
#     all_users = User.objects.exclude(id=request.user.id).only('id', 'username')
#     return render(request, 'video.html', {'allUsers': all_users})


# def pusher_auth(request):
#     payload = pusher_client.authenticate(
#         channel=request.POST['channel_name'],
#         socket_id=request.POST['socket_id'],
#         custom_data={
#             'user_id': request.user.id,
#             'user_info': {
#                 'id': request.user.id,
#                 'name': request.user.username
#             }
#         })
#     return JsonResponse(payload)


# def generate_agora_token(request):
#     appID = os.environ.get('17268e6e3f314edbb58da6fb080d4c82')
#     appCertificate = os.environ.get('23dd1f6e1c80423b9195e6a6216e6678')
#     channelName = json.loads(request.body.decode(
#         'utf-8'))['channelName']
#     userAccount = request.user.username
#     expireTimeInSeconds = 3600
#     currentTimestamp = int(time.time())
#     privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

#     token = RtcTokenBuilder.buildTokenWithAccount(
#         appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

#     return JsonResponse({'token': token, 'appID': appID})


# def call_user(request):
#     body = json.loads(request.body.decode('utf-8'))

#     user_to_call = body['user_to_call']
#     channel_name = body['channel_name']
#     caller = request.user.id

#     pusher_client.trigger(
#         'presence-online-channel',
#         'make-agora-call',
#         {
#             'userToCall': user_to_call,
#             'channelName': channel_name,
#             'from': caller
#         }
#     )
#     return JsonResponse({'message': 'call has been placed'})




from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from .agora_key import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def lobby(request):
    return render(request, 'lobby.html')

def room(request):
    return render(request, 'video.html') #it was room



def getToken(request):
    appId = "17268e6e3f314edbb58da6fb080d4c82"
    appCertificate = "23dd1f6e1c80423b9195e6a6216e6678"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)