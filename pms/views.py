from django.shortcuts import render, redirect
from django.contrib import messages
from allauth.account.decorators import login_required
from .models import  SaveData
from .forms import DataForm

def home(request):
    return render(request, 'home.html')
    
@login_required
def password(request):
    data_obj = SaveData.objects.filter(user = request.user)
    context = {'data_obj': data_obj}
    return render(request, 'password.html', context)

@login_required
def passwordform(request):
    form = DataForm()

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            new_pass = form.save(commit=False)
            new_pass.user = request.user
            new_pass.save()

            messages.success(request, 'Password was generated successfully')
            return redirect('password')

    context = {'form': form}
    return render(request, 'password_form.html', context)

@login_required
def password_update(request, id):
    data_obj = SaveData.objects.get(id=id)
    form = DataForm(instance=data_obj)

    if request.method == 'POST':
        form = DataForm(request.POST, instance=data_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password was updated successfully')
            return redirect('password')

    context = {'form': form}
    return render(request, 'password_form.html', context)


@login_required
def password_delete(request, id):
    data_obj = SaveData.objects.get(id=id)
    data_obj.delete()
    messages.info(request, 'Password was deleted successfully')
    return redirect('password')