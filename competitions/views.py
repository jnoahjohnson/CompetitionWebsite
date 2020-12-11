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
    if request.method == 'POST':
        new_competition = Competition()
        new_competition.name = request.POST.get('comp_name')
        new_competition.description = request.POST.get('comp_description')
        new_competition.points = request.POST.get('comp_points')

        new_competition.save()

        return redirect('competition_home')

    return render(request, 'competitions/new_competition.html')


def editCompetitions(request, competition_id):
    context = {
        'competitionData': defaultCompetitions[competition_id - 1]
    }

    return render(request, 'competitions/edit_competition.html', context)


def viewCompetitions(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    context = {
        'competitionData': competition
    }
    return render(request, 'competitions/view_competition.html', context)
