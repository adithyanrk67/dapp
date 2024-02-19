from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Create a new user record with the entered data
        User.objects.create(username=username, password=password)

        return redirect('user_details')  # Use username as the identifier
    return render(request, 'login.html')

def user_details(request):
    user = User.objects.all() # Query the user based on username
    return render(request, 'user_details.html', {'user': user})

