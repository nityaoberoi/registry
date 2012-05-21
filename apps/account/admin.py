from django.db import admin

from account.models import Account, Profile

class AccountAdmin(models.ModelAdmin):
    pass

class ProfileAdmin(models.ModelAdmin):
    pass

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)