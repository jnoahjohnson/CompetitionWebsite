from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'leaderboard/index.html')  
def editLeaderboardView(request) :
    return render(request, 'leaderboard/edit.html') 
def viewLeaderboardView(request) :
    return render(request, 'leaderboard/view.html' ) 

