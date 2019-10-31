from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Toast
from .serializers import ToastSerializer


def get_toast_and_increment():
    toast = Toast.objects.filter(disabled=False, explicit=False).order_by("?").first()
    if toast:
        toast.numUsed += 1
        toast.save()

    return toast


class HomepageView(View):
    template = "chest/chest.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {"toast": None})

    def post(self, request, *args, **kwargs):
        toast = get_toast_and_increment()
        return render(request, self.template, {"toast": toast})


class GetRandomView(APIView):
    def get(self, request):
        toast = get_toast_and_increment()
        serializer = ToastSerializer(toast)
        return Response(serializer.data)
