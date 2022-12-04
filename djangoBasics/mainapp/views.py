from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    # news previous data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_title"] = "что-то новенькое"
        context["news_description"] = {
            "description": "Тут будет описание"
        }
        context["range"] = range(5)
        context['datetime_obj'] = datetime.now()
        return context
