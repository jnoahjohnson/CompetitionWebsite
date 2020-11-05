from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('LEADERBOARD')  
def editLeaderboardView(request) :
    return HttpResponse('Edit Leaderboard') 
def viewLeaderboardView(request) :
    return HttpResponse('View Leaderboard') 

