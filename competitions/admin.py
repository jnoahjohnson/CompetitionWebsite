from django.contrib import admin
from .models import Competition, CompletedUsers, CompetitionCategory
# Register your models here.
admin.site.register(Competition)
admin.site.register(CompletedUsers)
admin.site.register(CompetitionCategory)
