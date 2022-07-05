from django.contrib import admin
from .models import  SaveData

@admin.register(SaveData)
class SaveDataAdmin(admin.ModelAdmin):
	model = SaveData
	list_display = ['website', 'username']