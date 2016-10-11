from django.contrib import admin

# Register your models here.

from models import UserType,UserInfo,UserGroup,Asset

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    search_fields = ('username', 'email')


class AssetAdmin(admin.ModelAdmin):
    list_display = ('hostname','ip','location','user_group')
    search_fields = ('hostname', 'ip')

admin.site.register(UserType,UserTypeAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(UserGroup)
admin.site.register(Asset,AssetAdmin)