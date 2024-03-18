from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, date


# organization table
class Company(models.Model):
    api_record_id = models.CharField(max_length=200, null=True, blank=True)
    last_querry_date = models.CharField(max_length=200, null=True, blank=True)
    cui = models.CharField(max_length=200, null=True, blank=True)
    denumire = models.CharField(max_length=200, null=True, blank=True)
    adresa = models.CharField(max_length=200, null=True, blank=True)
    nrRegCom = models.CharField(max_length=200, null=True, blank=True)
    telefon = models.CharField(max_length=200, null=True, blank=True)
    fax = models.CharField(max_length=200, null=True, blank=True)
    codPostal = models.CharField(max_length=200, null=True, blank=True)
    act = models.CharField(max_length=200, null=True, blank=True)
    stare_inregistrare = models.CharField(max_length=200, null=True, blank=True)
    data_inregistrare = models.CharField(max_length=200, null=True, blank=True)
    cod_CAEN = models.CharField(max_length=200, null=True, blank=True)
    iban = models.CharField(max_length=200, null=True, blank=True)
    statusRO_e_Factura = models.CharField(max_length=200, null=True, blank=True)
    organFiscalCompetent = models.CharField(max_length=200, null=True, blank=True)
    forma_de_proprietate = models.CharField(max_length=200, null=True, blank=True)
    forma_organizare = models.CharField(max_length=200, null=True, blank=True)
    forma_juridica = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.denumire}'
