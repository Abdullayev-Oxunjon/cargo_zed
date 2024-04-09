from rest_framework import serializers

from app.models import Party


class PartyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
