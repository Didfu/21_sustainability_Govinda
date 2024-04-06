from django.shortcuts import render

# Create your views her

def live_view(request):
    return render(request, 'web/live.html')

def month_view(request):
    return render(request, 'web/month.html')

def input_view(request):
    return render(request, 'web/input.html')

def govinda_view(request):
    return render(request, 'web/govinda.html')
