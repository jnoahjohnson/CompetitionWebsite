# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

defaultGroups = [
    {
        'name': 'GOATS',
        'icon': 'bacon'
    },
    {
        'name': 'Mandalorians',
        'icon': 'globe'
    }
]

def indexPageView(request) :
    context = {
        'groups': defaultGroups 
    }
    return render(request, 'connectfriends/index.html', context) 
def editConnectFriendsView(request) :
    return render(request, 'connectfriends/edit.html')
def createConnectFriendsView(request) :
    return render(request, 'connectfriends/create.html')
def joinConnectFriendsView(request) :
    return render(request, 'connectfriends/join.html')