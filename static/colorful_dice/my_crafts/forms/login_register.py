from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
        else:
            form = UserCreationForm()
        return render(request, 'login_register_form/register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        form = UserCreationForm(request.GET)
        if form.is_valid():
            return redirect('home_page.html')
        else:
            return redirect(request, 'register.html')
