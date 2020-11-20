from django.http import HttpResponse
from django.shortcuts import render



def indexPageView(request):
    return render(request, 'competitions/index.html')


def createCompetitions(request):
    return HttpResponse('Create Competition')


def editCompetitions(request, competition_id):
    context = {
        'competitionData': defaultCompetitions[competition_id - 1]
    }

    return render(request, 'competitions/edit_competition.html', context)


def viewCompetitions(request):
    return HttpResponse('View Competition')
