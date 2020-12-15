from django.shortcuts import render
from django.http import HttpResponse
from competitions.models import Competition
from django.contrib.auth.models import User


def view_leaderboard(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    completed_users = competition.completed_users.all()
    usernames = []
    # Geting all unique users that competed
    for user in completed_users:
        if not user in usernames:
            usernames.append(user)

    competitor_scores = []
    # Generate the score for each user based on how many times they appear in the linking table
    for competitor in usernames:
        times_completed = completed_users.filter(
            user=User.objects.get(id=competitor.user.id)).count()
        total_points = times_completed * competition.points

        competitor_data = {
            "competitor": competitor,
            "total_points": total_points
        }

        competitor_scores.append(competitor_data)

    # Pass all competitor data into context
    context = {
        "competition": competition,
        "competitor_scores": competitor_scores
    }
    return render(request, 'leaderboard/view.html', context)
