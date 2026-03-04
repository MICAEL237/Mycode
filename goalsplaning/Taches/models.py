from django.db import models
from Objectif.models import Goals

# Create your models here.



class Tasks (models.Model):
    liste = [
        ('en cours', 'En cours'),
        ('terminer', 'Terminer'),
        ('abandonner', 'Abandonner')
    ]
    titre = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    objectif = models.ForeignKey(Goals, on_delete=models.CASCADE,
                                 related_name='goalstasks',
                                 null=False)
    status = models.CharField(max_length=50, choices=liste)



    def __str__(self):
        return f'{self.titre}'

