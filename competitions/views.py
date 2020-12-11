from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Competition

defaultCompetitions = [
    {
        'id': 1,
        'name': 'Health',
        'percentComplete': 9,
        'icon': 'heart',
        'description': 'Get healthy!!!'
    },
    {
        'id': 2,
        'name': 'Scripture Study',
        'percentComplete': 55,
        'icon': 'book',
        'description': 'Get spiritual!!!'
    },
    {
        'id': 3,
        'name': 'Reading',
        'percentComplete': 21,
        'icon': 'book',
        'description': 'Read more!!!'
    }
]


def indexPageView(request):
    competitions = Competition.objects.all()

    context = {
        "competitions": competitions
    }

    return render(request, 'competitions/index.html', context)


def createCompetitions(request):
    if request.method == "POST" :
        competition = Competition()
        competition.name = request.POST.get('competition_name')
        competition.description = request.POST.get('competition_description')
        competition.points = request.POST.get('competition_points')

        competition.save()

        return redirect('/competitions/')


    return render(request, 'competitions/new_competition.html')


def editCompetitions(request, competition_id):
    context = {
        'competitionData': defaultCompetitions[competition_id - 1]
    }

    return render(request, 'competitions/edit_competition.html', context)


def viewCompetitions(request, competition_id):
    context = {
        'competitionData': defaultCompetitions[competition_id - 1]
    }
    return render(request, 'competitions/view_competition.html', context)
