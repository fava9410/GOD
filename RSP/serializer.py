from rest_framework import serializers
from .models import Match, Match_Detail

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match_Detail
        fields = ('round','round_winner','winner_move')
