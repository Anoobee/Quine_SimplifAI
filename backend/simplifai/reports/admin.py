from django.contrib import admin
from .models import Report, Chats, ReportText


# Register your models here.
admin.site.register(Report)   # this will make the Room model visible in the admin panel
admin.site.register(Chats)
admin.site.register(ReportText) 