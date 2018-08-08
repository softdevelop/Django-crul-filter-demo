from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_filter = ('sex','age')
admin.site.register(User,UserAdmin)