from django.contrib import admin
from web.models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display=["title","description"]

admin.site.register(Notification,NotificationAdmin)