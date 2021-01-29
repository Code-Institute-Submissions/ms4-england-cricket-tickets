from django.contrib import admin
from .models import Gametype, Match, Stadium, Ticket, Tour

# Register your models here.
admin.site.register(Gametype)
admin.site.register(Match)
admin.site.register(Stadium)
admin.site.register(Ticket)
admin.site.register(Tour)
