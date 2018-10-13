from django.contrib import admin
from .models import leaveschool,statistics,user
# Register your models here.

class leaveschoolAdmin(admin.ModelAdmin):
    list_display=('stuname','stusystem','stunation','classify','stugrade')
    list_filter=('stusystem',)

admin.site.register(leaveschool,leaveschoolAdmin)
class statisticsAdmin(admin.ModelAdmin):
    list_display=('ssystem','sgrade','stotal','ssum')
    list_filter=('ssystem',)
admin.site.register(statistics,statisticsAdmin)

class userAdmin(admin.ModelAdmin):
    list_display=('username','accountnum','password')
    list_filter=('username',)
admin.site.register(user,userAdmin)