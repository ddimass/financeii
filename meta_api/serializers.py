from .models import Bars
from rest_framework import serializers

class BarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bars
        fields = ('pair', 'timeframe', 'datetime', 'high', 'low', 'open', 'close')
