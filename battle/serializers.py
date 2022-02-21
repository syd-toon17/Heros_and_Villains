from rest_framework import serializers
from .models import Battle

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ['id', 'super_one', 'super_two', 'battle_date']