from urllib import request
from django.shortcuts import render

from .services import check

from .models import HeartDisease

# Create your views here.

def heart_disease_history(request):
    history_records = HeartDisease.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        history_records = history_records.filter(name__icontains=search_query)

    context = {
        'history_records': history_records,
        'search_query': search_query,
    }
    
    return render(request, 'heart_disease_history.html', context)


def heart(request):
    user_input, value = check(request)
    if user_input is not None:
        HeartDisease.objects.create(**user_input)

    context = {
        'predicted_value': value,
        'title': 'Heart Disease Prediction',
        'active': 'btn btn-success peach-gradient text-white',
        'heart': True,
    }

    return render(request, 'heart.html', context)


def home(request):
	return render(request,'home.html')  