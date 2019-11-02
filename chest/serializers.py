from rest_framework import serializers, viewsets
from rest_framework.response import Response

from chest.models import Toast


class ToastSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Toast
        fields = "__all__"
