from django.db import models
from authentification.models import Subscriber
# Create your models here.
class Traitement(models.Model):

    patient_id = models.PositiveIntegerField(default=0)
    doctor = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    creation_date= models.DateTimeField(auto_now=True)
    edit_date= models.DateTimeField(auto_now=True)
    traitement_content= models.FileField(blank=False,null=False)
    traitement_title = models.CharField(max_length=500,default="")

    TRAITEMENT_TYPE_CHOICES= (
        (1, 'ordonnance'),
        (2, 'massage'),
    )
    traitement_type = models.IntegerField(choices=TRAITEMENT_TYPE_CHOICES , default=1)