from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from entities.models import Hero


def index_view(request):
    context = {
        'a': 2
    }
    return render(request, 'entities/index.html', context)


class IndexTemplateView(TemplateView):
    template_name = 'entities/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = Hero.objects.first()
        return context


class IndexView(View):
    def get(self, request):
        context = {
            'a': 2
        }
        return render(request, 'entities/index.html', context)
