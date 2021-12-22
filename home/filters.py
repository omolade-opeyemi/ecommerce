import django_filters
from .models import *
from django.forms.widgets import TextInput

class productFilter(django_filters.FilterSet):
    prod_name = django_filters.CharFilter(field_name='prod_name',widget=TextInput(attrs={'placeholder': 'product name'}))
    #prod_cat = django_filters.CharFilter(field_name='prod_cat',widget=TextInput(attrs={'placeholder': 'product category'}))

    class Meta:
        model = Product
        fields = ('prod_name','prod_cat')
        widgets = {'prod_name': TextInput(attrs={'placeholder':'product name'})}
        