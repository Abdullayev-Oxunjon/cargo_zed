from rest_framework import serializers

from app.models import UzbekStorage


class UzbekStorageModelSerializer(serializers.ModelSerializer):
    client_keyword = serializers.CharField(source='client.keyword', read_only=True)
    trek_code = serializers.CharField(source='chinese_storage.trek_code', read_only=True)

    class Meta:
        model = UzbekStorage
        fields = ['id', 'client_keyword', 'trek_code', 'chinese_storage', 'client', 'party', 'price', 'status',
                  'created_at']
        extra_kwargs = {"chinese_storage": {"write_only": True},
                        "client": {"write_only": True}}
