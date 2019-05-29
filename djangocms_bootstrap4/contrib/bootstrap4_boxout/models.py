# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from js_color_picker.fields import RGBColorField

from djangocms_bootstrap4.fields import TagTypeField, AttributesField


@python_2_unicode_compatible
class Bootstrap4Boxout(CMSPlugin):
    """
    Components > "Boxout" Plugin
    https://getbootstrap.com/docs/4.0/components/boxout/
    """
    fluid = models.BooleanField(
        verbose_name=_('Fluid'),
        default=False,
        help_text=_('Adds the .boxout-fluid class.'),
    )
    full_width = models.BooleanField(
        verbose_name=_('Show Full Width'),
        default=False,
    )
    tag_type = TagTypeField()
    title = models.CharField(
        verbose_name=_('Title'),
        null=True,
        blank=True,
        max_length=255,
    )
    layout = models.CharField(
        verbose_name=_('Layout'),
        blank=True,
        max_length=255,
        help_text=_('Select a layout'),
    )
    background_color = RGBColorField(
        verbose_name=_('Background Color'),
        blank=True,
        null=True
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        if self.fluid:
            text = '({})'.format(_('Fluid'))
        return text
