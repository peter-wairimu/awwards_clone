from django. db import models
from .models import Project
import django_filters

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['project_name', 'project_photo', 'description', 'url', 'owner']
        filter_overrides = {
            models.ImageField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }