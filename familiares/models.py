from django.db import models
from django.utils import timezone
import datetime


class Familiar(models.Model): #definir classe e herança
    nome = models.CharField(max_length=150) #definir atributos
    idade = models.IntegerField()
    falecido = models.BooleanField(default=False)

    PRIMO = 'PO'
    PRIMA = 'PA'
    TIO = 'TIO'
    TIA = 'TIA'
    MAE = 'M'
    PAI = 'P'
    IRMAO = 'I'

    PARENTESCO_CHOICES = (
        (PRIMO, 'Primo'),
        (PRIMA, 'Prima'),
        (TIO, 'Tio'),
        (TIA, 'Tia'),
        (MAE, 'Mae'),
        (PAI, 'Pai'),
        (IRMAO, 'Irmao'),
    )
    parentesco = models.CharField(
        max_length=150,
        choices=PARENTESCO_CHOICES,
    )


    
    def __str__(self):
        return self.nome
