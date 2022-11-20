from rest_framework import serializers

from api.viewsets.training.model import Training


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = '__all__'
