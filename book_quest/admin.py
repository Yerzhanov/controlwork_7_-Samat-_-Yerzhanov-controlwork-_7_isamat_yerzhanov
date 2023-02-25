from django.contrib import admin

from book_quest.models import *

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)


admin.site.register(User_book)
admin.site.register(GuestBook)
