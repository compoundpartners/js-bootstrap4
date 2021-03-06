# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap4.constants import DEVICE_SIZES
from djangocms_bootstrap4.helpers import concat_classes

from .models import (
    Bootstrap4GridContainer,
    Bootstrap4GridRow,
    Bootstrap4GridColumn,
)
from .forms import (
    Bootstrap4GridRowForm,
    Bootstrap4GridColumnForm,
)
from .constants import(
    GRID_USE_ROW_BG_COLOR,
    GRID_USE_ROW_BG_IMAGE,
    GRID_USE_ROW_BG_VIDEO,
    GRID_USE_ROW_ICON,
    GRID_USE_ROW_ALIGNMENT,
    GRID_USE_ROW_TAG_TYPE,
    GRID_USE_ROW_GUTTER,
    GRID_USE_COL_BG_COLOR,
    GRID_USE_COL_BG_IMAGE,
    ADDITIONAL_CHILD_CLASSES,
    ADDITIONAL_PARENT_CLASSES,
)

class Bootstrap4GridContainerPlugin(CMSPluginBase):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridContainer
    name = _('Container')
    module = _('Bootstrap 4')
    render_template = 'djangocms_bootstrap4/grid_container.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'container_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        classes = concat_classes([
            instance.container_type,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super(Bootstrap4GridContainerPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4GridRowPlugin(CMSPluginBase):
    """
    Layout > Grid: "Row" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridRow
    name = _('Row')
    module = _('Bootstrap 4')
    form = Bootstrap4GridRowForm
    change_form_template = 'djangocms_bootstrap4/admin/grid_row.html'

    # Template handling
    render_template = 'djangocms_bootstrap4/grid_row.html'  # The default fallback template
    TEMPLATE_NAME = 'djangocms_bootstrap4/grid_row{separator}{variant}.html'
    def get_render_template(self, context, instance, placeholder):
        if instance.layout:
            separator = '__'
            template = self.TEMPLATE_NAME.format(separator=separator, variant=instance.layout)
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template
    # End template handling

    allow_children = True
    child_classes = ['Bootstrap4GridColumnPlugin'] + ADDITIONAL_CHILD_CLASSES.get('Bootstrap4GridRowPlugin', [])

    main_fields = (
        'layout',
        'create',
        'full_width',
        ('title', 'display_title'),
    )
    if GRID_USE_ROW_BG_COLOR:
        main_fields +=(
            'background_color',
        )
    if GRID_USE_ROW_BG_IMAGE:
        main_fields +=(
            ('background_image', 'parallax'),
        )
    if GRID_USE_ROW_BG_VIDEO:
        main_fields +=(
            'background_video',
        )
    if GRID_USE_ROW_ICON:
        main_fields +=(
            'icon',
        )
    advanced_fields = ()
    if GRID_USE_ROW_TAG_TYPE:
        advanced_fields += (
            'tag_type',
        )
    if GRID_USE_ROW_GUTTER:
        advanced_fields += (
            'gutters',
        )
    if GRID_USE_ROW_ALIGNMENT:
        advanced_fields += (
            ('vertical_alignment', 'horizontal_alignment'),
        )
    advanced_fields += (
        'attributes',
    )

    fieldsets = [
        (None, {
            'fields': main_fields,
        }),
        (_('Responsive settings'), {
            'classes': ('collapse',),
            'fields': (
                ['{}_hide'.format(size) for size in DEVICE_SIZES],
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': advanced_fields,
        }),
    ]

    def save_model(self, request, obj, form, change):
        super(Bootstrap4GridRowPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in range(int(data['create']) if data['create'] is not None else 0):
            extra = {}
            for size in DEVICE_SIZES:
                extra['{}_col'.format(size)] = data.get(
                    'create_{}_col'.format(size)
                )
            col = Bootstrap4GridColumn(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=obj.numchild,
                plugin_type=Bootstrap4GridColumnPlugin.__name__,
                **extra
            )
            obj.add_child(instance=col)

    def render(self, context, instance, placeholder):
        gutter = 'no-gutters' if instance.gutters else ''
        parallax = 'parallax' if instance.parallax else ''
        full_width = 'full-width' if instance.full_width else ''
        classes = []
        for device in DEVICE_SIZES:
            hide = getattr(instance, '{}_hide'.format(device))
            value = 'none' if hide else 'flex'
            if device == 'xs':
                classes.append('d-%s' % value)
                prev = hide
            else:
                if hide != prev:
                    classes.append('d-%s-%s' % (device, value))
                    prev = hide
        classes = concat_classes(classes + [
            'row',
            instance.vertical_alignment,
            instance.horizontal_alignment,
            gutter,
            parallax,
            full_width,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        styles = instance.attributes.get('style', '').split(' ')
        background = []
        if instance.background_color:
            background.append(instance.background_color)
        if instance.background_image:
            background.append('url(%s)' % instance.background_image.url)
        if background:
            styles.append('background: %s;' % ' '.join(background))
        instance.attributes['style'] = ' '.join(styles)

        return super(Bootstrap4GridRowPlugin, self).render(
            context, instance, placeholder
        )


class Bootstrap4GridColumnPlugin(CMSPluginBase):
    """
    Layout > Grid: "Column" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    model = Bootstrap4GridColumn
    name = _('Column')
    module = _('Bootstrap 4')
    form = Bootstrap4GridColumnForm
    change_form_template = 'djangocms_bootstrap4/admin/grid_column.html'
    render_template = 'djangocms_bootstrap4/grid_column.html'
    TEMPLATE_NAME = 'djangocms_bootstrap4/grid_column{separator}{variant}.html'
    allow_children = True
    require_parent = True
    # TODO it should allow for the responsive utilitiy class
    # https://getbootstrap.com/docs/4.0/layout/grid/#column-resets
    parent_classes = ['Bootstrap4GridRowPlugin'] + ADDITIONAL_PARENT_CLASSES.get('Bootstrap4GridColumnPlugin', [])

    advanced_fields = (
        'tag_type',
        ('title', 'display_title'),
    )
    if GRID_USE_COL_BG_COLOR:
        advanced_fields +=(
            'background_color',
        )
    if GRID_USE_COL_BG_IMAGE:
        advanced_fields +=(
            'background_image',
        )
    advanced_fields +=(
        'attributes',
    )
    fieldsets = [
        (None, {
            'fields': (
                'layout',
                'column_type',
                ('column_size', 'column_alignment'),
            )
        }),
        (_('Responsive settings'), {
            'classes': ('collapse',),
            'fields': (
                ['{}_col'.format(size) for size in DEVICE_SIZES],
                ['{}_order'.format(size) for size in DEVICE_SIZES],
                ['{}_ml'.format(size) for size in DEVICE_SIZES],
                ['{}_mr'.format(size) for size in DEVICE_SIZES],
                ['{}_hide'.format(size) for size in DEVICE_SIZES],
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': advanced_fields
        }),
    ]

    def render(self, context, instance, placeholder):
        column = ''
        classes = instance.get_grid_values()

        if instance.column_size:
            column = 'col-{}'.format(instance.column_size)
        if classes:
            column += ' {}'.format(' '.join(cls for cls in classes if cls))

        attr_classes = concat_classes([
            instance.column_type,
            column,
            instance.column_alignment,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = attr_classes

        styles = instance.attributes.get('style', '').split(' ')
        background = []
        if instance.background_color:
            background.append(instance.background_color)
        if instance.background_image:
            background.append('url(%s)' % instance.background_image.url)
        if background:
            styles.append('background: %s;' % ' '.join(background))
        instance.attributes['style'] = ' '.join(styles)

        return super(Bootstrap4GridColumnPlugin, self).render(
            context, instance, placeholder
        )

    def get_render_template(self, context, instance, placeholder):
        separator = ''
        if instance.layout:
            separator = '__'
            template = self.TEMPLATE_NAME.format(separator=separator, variant=instance.layout)
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template

plugin_pool.register_plugin(Bootstrap4GridContainerPlugin)
plugin_pool.register_plugin(Bootstrap4GridRowPlugin)
plugin_pool.register_plugin(Bootstrap4GridColumnPlugin)
