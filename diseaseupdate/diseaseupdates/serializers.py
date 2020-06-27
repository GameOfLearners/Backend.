from rest_framework import serializers
from .models import Diseaseupdates


class DiseaseupdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diseaseupdates
        fields = ('id', 'symptoms', 'trends', 'measures')