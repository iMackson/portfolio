from django.shortcuts import render
# from django.http import HttpResponse
from .models import Person, Portfolio
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    persons = Person.objects.all()
    portfolios = Portfolio.objects.all()
    form = ContactForm()
    context = {
        'persons': persons, 
        'portfolios': portfolios,
        'form': form
    }
    return render(request, 'core/index.html', context)


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email_address = form.cleaned_data.get('email_address')
            country = form.cleaned_data.get('country')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')

            subject = "A Visitor's Comment"

            message = name + " with the email " + email_address + " sent the following message: \n\n" + message

            send_mail(subject, message, 'isanimackson@gmail.com', [email_address])

            context = {'form': form}

            return render(request, 'core/index.html', context)
        else:
            form = ContactForm()
        return render(request, 'core/index.html', {'form': form})