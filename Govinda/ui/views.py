from django.shortcuts import render
import PowerPredictionModel, StabilityPredictorModel
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
        
        # Load the Power Prediction Model
        power_model = PowerPredictionModel.objects.last()
        if not power_model:
            return render(request, 'web/error.html', {'message': 'No Power Prediction Model found.'})

        # Predict power
        power_input_data = {
            'DateTime': [date + ' ' + time],
            'Air temperature': [air_temp],
            'Wind speed': [wind_speed],
            'Pressure': [wind_pressure]
        }
        n1, n2, n3 = power_model.predict_power(pd.DataFrame(power_input_data))

        # Load the Stability Predictor Model
        stability_model = StabilityPredictorModel.objects.last()
        if not stability_model:
            return render(request, 'web/error.html', {'message': 'No Stability Predictor Model found.'})

        # Predict stability
        stability_input_data = {
            'date': [date + ' ' + time],
            'n1': [n1],
            'n2': [n2],
            'n3': [n3],
            # Assuming you have additional fields required for stability prediction
            'c1': ...,  # Fill in the values accordingly
            'c2': ...,
            'c3': ...,
            'p1': ...,
            'p2': ...,
            'p3': ...
        }
        predicted_stability = stability_model.predict_stability(pd.DataFrame(stability_input_data), n1, n2, n3)

        return render(request, 'web/result.html', {'n1': n1, 'n2': n2, 'n3': n3, 'predicted_stability': predicted_stability})
    
    return render(request, 'web/input.html')

def input_view(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        air_temp = float(request.POST.get('airTemperature'))
        wind_speed = float(request.POST.get('windSpeed'))
        wind_pressure = float(request.POST.get('airpressure'))
        
        # Load the Power Prediction Model
        power_model = PowerPredictionModel.objects.last()
        if not power_model:
            return render(request, 'web/error.html', {'message': 'No Power Prediction Model found.'})

        # Predict power
        power_input_data = {
            'DateTime': [date + ' ' + time],
            'Air temperature': [air_temp],
            'Wind speed': [wind_speed],
            'Pressure': [wind_pressure]
        }
        n1, n2, n3 = power_model.predict_power(pd.DataFrame(power_input_data))

        # Load the Stability Predictor Model
        stability_model = StabilityPredictorModel.objects.last()
        if not stability_model:
            return render(request, 'web/error.html', {'message': 'No Stability Predictor Model found.'})

        # Predict stability
        stability_input_data = {
            'date': [date + ' ' + time],
            'n1': [n1],
            'n2': [n2],
            'n3': [n3],
            # Assuming you have additional fields required for stability prediction
            'c1': ...,  # Fill in the values accordingly
            'c2': ...,
            'c3': ...,
            'p1': ...,
            'p2': ...,
            'p3': ...
        }
        predicted_stability = stability_model.predict_stability(pd.DataFrame(stability_input_data), n1, n2, n3)

        # Determine sustainability
        result = "Sustainable" if predicted_stability == 1 else "Unsustainable"
        
        return render(request, 'web/input.html', {'result': result})
    
    return render(request, 'web/input.html')

def govinda_view(request):
    return render(request, 'web/govinda.html')
