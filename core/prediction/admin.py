from django.contrib import admin
from .models import HeartDisease

@admin.register(HeartDisease)
class HeartDiseaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'sex', 'date']
    search_fields = ['name'] 
    list_filter = ['sex']