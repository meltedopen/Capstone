from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def home_page(request):
    # print(request.session.get("first_name", "Unknown")) # get
    context = {
        "title": "Home Page",
        "content": "Welcome to the Home Page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEET"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Welcome to the About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Welcome to the ContactPage",
        "form": contact_form,
        "brand": "new Brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     # print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
