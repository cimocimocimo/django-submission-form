from django.views.generic.base import TemplateView

from django.apps import apps
from django.urls import reverse

# List all the form demos
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        forms = []
        for label, config in apps.app_configs.items():
            if config.path.find('/site-packages/') == -1 and label != 'home':
                forms.append({
                    'name': config.verbose_name,
                    'label': config.label,
                    'file_path': config.path,
                    'python_path': config.name,
                    'url': reverse('index', current_app=config.name),
                })

        context['forms'] = forms

        return context

