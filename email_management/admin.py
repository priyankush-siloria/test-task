from django.contrib import admin
from .models import *


class SendEmailAdmin(admin.ModelAdmin):
	list_display = ('id', 'users', 'message', 'status', 'updated_at')

admin.site.register(SendEmail, SendEmailAdmin)


class SenderEmailAdmin(admin.ModelAdmin):
	list_display = ('id', 'sender')

admin.site.register(SenderEmail, SenderEmailAdmin)