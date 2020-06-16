from authentification import serializers
from .models import Traitement
from rest_framework import serializers
from .models import Subscriber
from authentification.serializers import DoctorRegistrationSerializer


class TraitementSerializer(serializers.ModelSerializer):
    # id_patient = serializers.CharField(write_only=True,default="2")
    # id_doctor = serializers.CharField(write_only=True,default="3")
    # patient_obj= serializers.SerializerMethodField('get_patient_object')
    # def get_patient_object(self):
    #     obj=Subscriber.objects.filter(pk=self.re)

    class Meta:
        model = Traitement
        # fields= "__all__"
        fields = ['pk',
                  'traitement_title',
                  'traitement_type',
                  'traitement_content',
                  'id_doctor',
                  'id_patient'
                  ]
