import django_filters
from django_filters import DateFilter, CharFilter
from blog.models import *

class ArticleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    note = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Article
        fields = '__all__'