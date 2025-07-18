from django.views.generic import TemplateView
from django.http import HttpResponse

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
