from rest_framework import serializers

from app.models import ChineseStorage


class ChineseStorageModelSerializer(serializers.ModelSerializer):
    client_keyword = serializers.CharField(source='client.keyword', read_only=True)

    class Meta:
        model = ChineseStorage
        fields = ["id", 'trek_code', 'product_title', "product_count",
                  "product_weight", "client_keyword", "client", "party", "box", "created_at"]
        extra_kwargs = {"trek_code": {"read_only": True},
                        "client": {"write_only": True}}
