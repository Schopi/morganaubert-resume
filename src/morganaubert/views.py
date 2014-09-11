# -*- coding: utf-8 -*-

# Standard library imports
from datetime import datetime

# Third party imports
from dateutil.relativedelta import relativedelta
from django.utils.timezone import get_default_timezone
from django.utils.timezone import make_aware
from django.utils.timezone import now
from django.views.generic import TemplateView

# Local application / specific library imports


class HomeView(TemplateView):
    template_name = 'morganaubert/home.html'

    birdhday_date = datetime(day=7, month=7, year=1989)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['age'] = relativedelta(
            now(), make_aware(self.birdhday_date, get_default_timezone())).years
        context['current_year'] = now().year

        return context
