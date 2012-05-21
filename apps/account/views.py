from django.views.generic.base import TemplateView


class Home(TemplateView):

    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

