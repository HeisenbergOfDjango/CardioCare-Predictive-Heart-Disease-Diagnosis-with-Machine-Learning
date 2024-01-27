import datetime
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


def user_inputs(request):
    user_input = {
            'name': request.POST.get('name', ''),
            'age': float(request.POST.get('age', 0)),
            'sex': float(request.POST.get('sex', 0)),
            'cp': float(request.POST.get('cp', 0)),
            'trestbps': float(request.POST.get('trestbps', 0)),
            'chol': float(request.POST.get('chol', 0)),
            'fbs': float(request.POST.get('fbs', 0)),
            'restecg': float(request.POST.get('restecg', 0)),
            'thalach': float(request.POST.get('thalach', 0)),
            'exang': float(request.POST.get('exang', 0)),
            'oldpeak': float(request.POST.get('oldpeak', 0)),
            'slope': float(request.POST.get('slope', 0)),
            'ca': float(request.POST.get('ca', 0)),
            'thal': float(request.POST.get('thal', 0)),
        }
    return user_input


def check(request):
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]

    value = ''
    if request.method == 'POST':
        user_input = user_inputs(request)
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

        return user_input, value
    return None, value