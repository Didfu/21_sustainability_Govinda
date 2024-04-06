from django.shortcuts import render

# Create your views her

def live_view(request):
    return render(request, 'web/live.html')

def month_view(request):
    return render(request, 'web/month.html')

def input_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        air_temp = request.POST.get('airTemperature')
        wind_speed = request.POST.get('windSpeed')

    return render(request, 'web/input.html')

def govinda_view(request):
    return render(request, 'web/govinda.html')
