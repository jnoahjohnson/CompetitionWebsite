# Create your views here.
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Connect Friends!') 
def editConnectFriendsView(request) :
    return HttpResponse('Edit Group') 
def createConnectFriendsView(request) :
    return HttpResponse('Create Group') 
def joinConnectFriendsView(request) :
    return HttpResponse('Join Group') 