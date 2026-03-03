from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Goals(models.Model):
    liste = [
        ('En cours','En cours' ),
        ('Termier','Terminer' )

    ]
    titre = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    date_debut = models.DateField( blank=False, null=False)
    date_fin = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='usergoal',
                             null=False
                             )
    etat = models.CharField(max_length=50, choices=liste, default='En cours')



    def __str__(self):
        return {self.titre}