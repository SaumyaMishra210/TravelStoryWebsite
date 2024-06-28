from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.utils import IntegrityError
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "invalid credentials")
            print('Login successfully')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']

        # Check if passwords match
        if pass1 == pass2:
            user_exists = User.objects.filter(username=username).exists()
            email_exists = User.objects.filter(email=email).exists()

            # Check if username already exists
            if user_exists:
                error_message = "Username '{}' already exists. Please choose a different username.".format(username)
                messages.error(request, 'User exists')
                # return redirect('register')
                return render(request,'register.html')

            elif email_exists:
                error_message = "Email '{}' already exists. Please choose a different email.".format(email)
                messages.error(request, 'Email exists')
                # return redirect('register')
                return render(request, 'register.html')

            else:
                # Create user
                user = User.objects.create_user(username=username, password=pass1, email=email )
                user.save()
                print('User created successfully')
                messages.success(request, 'Registration successful')
                return render(request,'login.html')  # Redirect after successful registration
        else:
            # return redirect('register')
            print('Password Mismatch.')
            messages.error(request, 'Password Mismatch.')

            return render(request, 'register.html')
    else:
        # return redirect('register')
        return render(request, 'register.html')

def logout(request):
    # return render(request,'index.html')
    auth.logout(request)
    return redirect('/')