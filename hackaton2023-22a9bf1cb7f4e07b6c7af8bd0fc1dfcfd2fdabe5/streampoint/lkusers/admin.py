from django.contrib import admin
from .models import ContribUsers, History


@admin.register(ContribUsers)
class ContribUsers(admin.ModelAdmin):
    list_display = ("user", "points")
    list_filter = ["points"]

@admin.register(History)
class ContribUsers(admin.ModelAdmin):
    list_display = ("user", "points")
    list_filter = ["quiz"]

