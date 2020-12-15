from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Competition, CompetitionCategory, CompletedUsers
from authorization.models import Competitor
from django.contrib.auth.models import User


def competition_about(request):
    return render(request, 'competitions/about.html')


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
        competition.creator = Competitor.objects.get(user=request.user.id)
        competition.competition_category = CompetitionCategory.objects.get(id=request.POST.get(
            'competition_category'))

        competition.save()

        return redirect('/competitions/')

    context = {
        "competition_categories": CompetitionCategory.objects.all()
    }

    return render(request, 'competitions/new_competition.html', context)


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

    from datetime import date
    competition = Competition.objects.get(id=competition_id)

    # Check and see if this is the creator of the competition
    is_creator = False

    if request.user.id == competition.creator.user.id:
        is_creator = True

    # Check to see iuf the user has completed the task already for the day
    completed_task = False

    if CompletedUsers.objects.filter(competition=competition.id,
                                     competitor=Competitor.objects.get(user=request.user.id), date=date.today()).count() > 0:
        completed_task = True

    context = {
        'competition': competition,
        'is_creator': is_creator,
        'completed_task': completed_task
    }

    return render(request, 'competitions/view_competition.html', context)


def task_completed(request, competition_id):
    print('here')
    if request.method == 'POST':
        from datetime import date
        competition = Competition.objects.get(id=competition_id)
        competitor = Competitor.objects.get(user=request.user.id)

        completed_users = CompletedUsers()

        completed_users.competition = competition
        completed_users.competitor = competitor
        completed_users.date = date.today()

        completed_users.save()

    return redirect('competition_view', competition_id=competition_id)
