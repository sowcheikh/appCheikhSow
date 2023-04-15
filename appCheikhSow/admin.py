from django.contrib import admin
from .models import Commande, SuivisCommande, Contact
# Register your models here.
admin.site.register(Commande, SuivisCommande)
admin.site.register(Contact)
