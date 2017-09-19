from django.views.generic import View


class IndexView(View):
    template_name = 'index.html'
