from rest_framework import serializers

from api.viewsets.label.model import Label


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ('uuid', 'name', 'dataset')
        extra_kwargs = {
            'dataset': {'write_only': True}
        }
