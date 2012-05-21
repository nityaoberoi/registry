from django.db import admin

from gift.models import GiftList, Item

class GiftListAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(GiftList, GiftListAdmin)
admin.site.register(Item, ItemAdmin)