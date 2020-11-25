from django.contrib import admin
from .models import Competition, Task, UserTask
# Register your models here.
admin.site.register(Competition)
admin.site.register(Task)
admin.site.register(UserTask)