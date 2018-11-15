from django.shortcuts import render
from django.http import JsonResponse
from chest.models import Toast
from chest.api import ToastSerializer


def chest(request):
    error = None
    if request.method == 'GET':
        toast = Toast.objects.none()
    elif request.method == 'POST':
        toast = get_and_update()
        if not toast:
            error = "No toasts available!"

    return render(request, 'chest/chest.html', {'toast': toast, 'error': error})


def api_get_random(request):
    toast = get_and_update()
    if toast:
        serializer = ToastSerializer(toast)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse('No toasts available', safe=False)


def get_and_update():
    toast = Toast.objects.filter(disabled=False, explicit=False).order_by('?').first()
    if toast:
        toast.numUsed += 1
        toast.save()

    return toast