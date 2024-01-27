from urllib import request
from django.shortcuts import render

from .services import check

from .models import HeartDisease


# Create your views here.


def heart(request):
    user_input, value = check(request)
    if user_input is not None:
        HeartDisease.objects.create(**user_input)

    temp_data = {
        'predicted_value': value,
        'title': 'Heart Disease Prediction',
        'active': 'btn btn-success peach-gradient text-white',
        'heart': True,
    }

    return render(request, 'heart.html', temp_data)


def home(request):
	return render(request,'home.html')  