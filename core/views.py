from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse
from .forms import SignUpForm

class LandingPageView(TemplateView):
    template_name = "core/landing.html"

def subscribe(request):
    if request.method == "POST":
        # This is a simple example - you would typically handle email subscription here
        return HttpResponse(
            """
            <div class="text-green-600 font-medium">
                Thanks for subscribing! We'll be in touch soon.
            </div>
            """,
            content_type="text/html"
        )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
