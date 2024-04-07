from django.shortcuts import render
import pandas as pd
# Create your views her

def live_view(request):
    return render(request, 'web/live.html')

def month_view(request):
    return render(request, 'web/month.html')

def input_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        air_temp = float(request.POST.get('airTemperature'))
        wind_speed = float(request.POST.get('windSpeed'))
        wind_pressure = float(request.POST.get('airpressure'))
        
        
    return render(request, 'web/input.html')

def govinda_view(request):
    return render(request, 'web/govinda.html')
