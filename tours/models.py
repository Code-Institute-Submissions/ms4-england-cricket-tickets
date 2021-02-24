from django.db import models

# Create your models here.


class Gametype(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tour(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Match(models.Model):
    class Meta:
        verbose_name_plural = 'Matches'
    tour = models.ForeignKey(
        'Tour', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    stadium = models.ForeignKey(
        'Stadium', null=True, blank=False, on_delete=models.SET_NULL)
    date = models.CharField(max_length=254)
    gametype = models.ForeignKey(
        'Gametype', null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    match = models.ForeignKey(
        'Match', null=True, blank=False, on_delete=models.SET_NULL)
    stadium = models.ForeignKey(
        'Stadium', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, )
    friendly_name = models.CharField(max_length=254, null=True, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
