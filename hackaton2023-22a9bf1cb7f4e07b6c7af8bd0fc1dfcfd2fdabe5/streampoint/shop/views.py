from django.http import JsonResponse
from django.shortcuts import render
def save_coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        # Здесь можно сохранить координаты в базе данных или выполнить другие действия
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Неверный метод запроса'})


def ponil(requst):
    return render(requst, 'shop/streamers.html')