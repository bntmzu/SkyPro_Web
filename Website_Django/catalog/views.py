from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')

        messages.success(request, "Your message has been sent successfully!")
        return redirect('catalog:contacts')

    return render(request, 'contacts.html')
