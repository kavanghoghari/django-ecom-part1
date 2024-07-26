from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Ensure you import your form class

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Instantiate the form with POST data
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # Ensure this name matches the name in your urls.py
    else:
        form = RegistrationForm()  # Instantiate an empty form for a GET request

    return render(request, 'core/index.html', {'form': form})
