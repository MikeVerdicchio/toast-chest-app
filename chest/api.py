from rest_framework import serializers, viewsets
from rest_framework.response import Response
from chest.models import Toast


class ToastSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Toast
        fields = '__all__'


class ToastViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Toast.objects.all()
    serializer_class = ToastSerializer

    def retrieve(self, request, pk=None):
        if pk == '0':
            toast = Toast.objects.filter(disabled=False).order_by('?').first()
            toast.numUsed += 1
            toast.save()
            serializer = ToastSerializer(toast)
            return Response(serializer.data)
        else:
            return super(ToastViewSet, self).retrieve(request, pk)
