from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'question',
        'answer'
    )
    ordering = ('name',)
    

# Register your models here.
admin.site.register(FAQ, FAQAdmin)
