from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def base(request):
    template_name = 'base.html'
    return render(request, template_name)


def presentation(request):
    template_name = 'presentation.html'
    return render(request, template_name)


def tome1(request):
    template_name = 'tome1.html'
    return render(request, template_name)


def tome2(request):
    template_name = 'tome2.html'
    return render(request, template_name)


def contact(request):
    form = ContactForm()
    context = {'form': form}
    template_name = 'contact.html'
    # if request.method == "POST":
    #     nom = request.POST.get('nom')
    #     email = request.POST.get('email')
    #     sujet = request.POST.get('sujet')
    #     message = request.POST.get('message')
    #     form.nom = nom
    #     form.email = email
    #     form.sujet = sujet
    #     form.message = message
    #     form.save()
    #     return redirect("thanks")
    # return render(request, template_name, context)
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            sujet = request.POST.get('sujet')
            message = request.POST.get('message')
            form.nom = nom
            form.email = email
            form.sujet = sujet
            form.message = message
            form.save()
            return redirect("thanks")
        print('form =====', form)
    return render(request, template_name, context)


def thanks(request):
    return HttpResponse("Success! Thank you for your message.")


def to_admin(request):
    return redirect("admin")


def signout(request):
    return redirect("admin")