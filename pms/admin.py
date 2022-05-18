from django.contrib import admin
from .models import  SaveData

# Register your models here.
admin.site.register(SaveData)

class SaveDataAdmin(admin.ModelAdmin):
	model = SaveData
	list_display = ['website', 'username']