from django import forms
from .models import Tour, Ticket, Match, Stadium, Gametype


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tours = Tour.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in tours]

        self.fields['tour'].choices = friendly_names
        
