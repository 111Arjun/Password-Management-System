from django.urls import path
from .views import passwordform, home, password_delete, password, password_update

urlpatterns = [
    path('', home, name="home"),
    path('password/', password, name="password"),
	path('password-form/', passwordform, name='password_form'),
    path('delete/<int:id>/', password_delete, name='password_delete'),
    path('password/update/<int:id>/', password_update, name='password_update'),
]