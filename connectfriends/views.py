# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'connectfriends/index.html') 
def editConnectFriendsView(request) :
    return render(request, 'connectfriends/edit.html')
def createConnectFriendsView(request) :
    return render(request, 'connectfriends/create.html')
def joinConnectFriendsView(request) :
    return render(request, 'connectfriends/join.html')