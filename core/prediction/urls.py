from django.urls import path
from .views import heart, home, heart_disease_history
 
urlpatterns = [
    path(
        'heart', 
        heart, 
        name="heart"
    ),
    path(
        '',
        home, 
        name="home"
    ),
    path(
        'heart-disease-history', 
        heart_disease_history, 
        name='heart_disease_history'
    )
]