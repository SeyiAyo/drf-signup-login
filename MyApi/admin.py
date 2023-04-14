from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name']
    search_fields = ['email', 'first_name', 'last_name']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
