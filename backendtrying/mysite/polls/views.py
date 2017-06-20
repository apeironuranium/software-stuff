from django.views import generic
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "polls/index.html"


class CreditsView(generic.TemplateView):
    template_name = "polls/credits.html"
