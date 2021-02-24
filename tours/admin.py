from django.contrib import admin
from .models import Gametype, Match, Stadium, Ticket, Tour


class GameTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )
    ordering = ('name',)


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'tour',
        'name',
        'stadium',
        'date',
        'gametype'
    )
    ordering = ('tour', 'gametype', 'name')


class StadiumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'full_name',
        'image',
        'image_url'
    )
    ordering = ('name',)


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'stadium',
        'name',
        'friendly_name',
        'price',
        'match'
    )
    ordering = ('name',)


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_url'
    )
    ordering = ('name',)


# Register your models here.
admin.site.register(Gametype, GameTypeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Tour, TourAdmin)
