from django.http import HttpResponse


def indexPageView(request):
    return HttpResponse('Competition Index')


def createCompetitions(request):
    return HttpResponse('Create Competition')


def editCompetitions(request):
    return HttpResponse('Edit Competitions')


def viewCompetitions(request):
    return HttpResponse('View Competition')
