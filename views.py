from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from userauths.forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('index')  # Redirect to the index view after successful signup
    else:
        form = UserRegisterForm()
    
    return render(request, 'userauths/sign-up.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")      
            return render(request, "userauths/sign-in.html")

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("index")  # Redirect to the index view after successful login
        else:
            messages.warning(request, "Invalid credentials")

    context = {}
    return render(request, "userauths/sign-in.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('userauths:sign-in')
