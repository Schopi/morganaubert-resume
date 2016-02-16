# -*- coding: utf-8 -*-

from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class MorganaubertViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)
