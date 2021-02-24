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


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StadiumForm(forms.ModelForm):

    class Meta:
        model = Stadium
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
