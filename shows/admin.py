from django.contrib import admin
from .models import Show


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'date',
        'location',
        'venue',
        'tickets_url'
    )

    ordering = ('-date')


admin.site.register(Show)
