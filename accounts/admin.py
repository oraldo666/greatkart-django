from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    # What to display on admin pannel
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login','date_joined', 'is_active', )
    # What items to be links clicked and to go to the product
    list_display_links = ('email', 'first_name', 'last_name',)
    read_only_fields = ('last_login', 'date_joined', )
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

