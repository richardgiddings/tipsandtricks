from .models import Section, Tip, Trick
from rest_framework import serializers

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title',)

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('id', 'title', 'notes', 'section')

class TrickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trick
        fields = ('id', 'command', 'tip')

class TipTrickSerializer(serializers.ModelSerializer):

    # link tips to tricks
    tricks = TrickSerializer(many=True, read_only=True)

    class Meta:
        model = Tip
        fields = ('id', 'title', 'notes', 'section', 'tricks')
