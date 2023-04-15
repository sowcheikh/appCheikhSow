from django.db import models
from django.contrib import admin
# Create your models here.


class Commande(models.Model):
    idCom = models.CharField(max_length=10)
    livreCom = models.CharField(max_length=50)
    qteCom = models.IntegerField(50)
    dateCom = models.DateTimeField()
    nomClient = models.CharField(max_length=20)
    prenomClient = models.CharField(max_length=30)
    telephoneClient = models.IntegerField()
    adresseClient = models.CharField(max_length=50)
    moyenPaiementClient = models.CharField(max_length=50)


class SuivisCommande(admin.ModelAdmin):
    list_display = ('idCom', 'livreCom', 'qteCom', 'dateCom', 'nomClient', 'prenomClient', 'telephoneClient',
                    'adresseClient', 'moyenPaiementClient')
    list_filter = ('livreCom', 'qteCom', 'dateCom', 'nomClient', 'prenomClient')
    search_fields = ('livreCom', 'qteCom', 'dateCom', 'nomClient', 'prenomClient')


class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.nom} message"