from django.shortcuts import render
from django.http import HttpResponse
from .models import LeaderBoard

def homeLeaderboardView(request) :
    # competitioner = LeaderBoard.competition.objects.get(id=competition_id)
    context = {
                "competition" : competition
            } 
    return render(request, 'leaderboard/home.html', context)  
def editLeaderboardView(request) :
    return render(request, 'leaderboard/edit.html') 
def viewLeaderboardView(request) :
    return render(request, 'leaderboard/view.html' ) 

