from django.db import models
from Taches.models import Tasks

# Create your models here.


class Sessions(models.Model):
 
    tache = models.ForeignKey(Tasks, on_delete=models.CASCADE, 
                              related_name='sessiontask', null=False, blank=False)
    
    heure_debut = models.TimeField(blank=False, null=False,  auto_now=True)
    heure_fin = models.TimeField(blank=False, null=True)


    