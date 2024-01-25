import datetime
from urllib import request
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from .models import HeartDisease

# Create your views here.

def heart(request):
     
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]

    #predicted_value = None
    value = ''
    if request.method == 'POST':
        user_input = {
            'name': request.POST.get('name', ''),
            'age': float(request.POST['age']),
            'sex': float(request.POST['sex']),
            'cp': float(request.POST['cp']),
            'trestbps': float(request.POST['trestbps']),
            'chol': float(request.POST['chol']),
            'fbs': float(request.POST['fbs']),
            'restecg': float(request.POST['restecg']),
            'thalach': float(request.POST['thalach']),
            'exang': float(request.POST['exang']),
            'oldpeak': float(request.POST['oldpeak']),
            'slope': float(request.POST['slope']),
            'ca': float(request.POST['ca']),
            'thal': float(request.POST['thal']),
        }

        user_data = user_input.copy()
        user_data.pop('name', None)
        user_data = np.array(list(user_data.values())).reshape(1, len(user_data))

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predicted_value = rf.predict(user_data)

        predicted_value = int(predicted_value[0])

        if predicted_value == 1:
            value = 'have'
        elif predicted_value == 0:
            value = "don't have"

        user_input['date'] = datetime.datetime.now()
        user_input['predicted_value'] = predicted_value
        HeartDisease.objects.create(**user_input)
        
    return render(request, 'heart.html', {
        'predicted_value': value if (value == 1 or value == 0) else -5,
        'title': 'Heart Disease Prediction',
        'active': 'btn btn-success peach-gradient text-white',
        'heart': True,
    })


def home(request):
	return render(request,
				'home.html')     