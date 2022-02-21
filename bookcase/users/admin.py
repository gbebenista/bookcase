from django.contrib import admin
from .forms import UserCreation, UserChange
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class UserAdministrator(UserAdmin):
    add_form = UserCreation
    form = UserChange
    model = CustomUser
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_active']
    list_filter = ('username',)


admin.site.register(CustomUser, UserAdministrator)
