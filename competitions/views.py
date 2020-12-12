from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Competition


def competition_home_view(request):
    if not request.user.is_authenticated:
        return redirect('index')

    competitions = Competition.objects.all()

    context = {
        "competitions": competitions
    }

    return render(request, 'competitions/competition_home.html', context)


def createCompetitions(request):
    if request.method == "POST":
        competition = Competition()
        competition.name = request.POST.get('competition_name')
        competition.description = request.POST.get('competition_description')
        competition.points = request.POST.get('competition_points')

        competition.save()

        return redirect('/competitions/')

    return render(request, 'competitions/new_competition.html')


def editCompetitions(request, competition_id):
    if request.method == 'POST':
        competition = Competition.objects.get(id=competition_id)
        competition.name = request.POST.get('competition_name')
        competition.description = request.POST.get('competition_description')
        competition.points = request.POST.get('competition_points')
        competition.save()

        return redirect('competition_view', competition_id=competition_id)

    competition = Competition.objects.get(id=competition_id)

    context = {
        'competition': competition
    }

    return render(request, 'competitions/edit_competition.html', context)


def deleteCompetition(request, competition_id):
    if request.method == 'POST':
        Competition.objects.get(id=competition_id).delete()

        return redirect('competition_home')

    return redirect('competition_view', competition_id=competition_id)


def viewCompetitions(request, competition_id):
    competition = Competition.objects.get(id=competition_id)

    context = {
        'competition': competition
    }

    return render(request, 'competitions/view_competition.html', context)
