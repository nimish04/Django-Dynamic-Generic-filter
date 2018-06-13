from core.models import *
from django import forms
import django_filters

price = (
    ((0, 999), 'Rs 0-999'),
    ((1000, 2499), 'Rs 1000-2499'),
    ((2500, 10000), 'Rs 2500-10000'),
    ((int(10001), int(50000)), 'Rs 10001-50000'),
    ((500001,1000000),'Rs 50000+'),
)

people=(
    ((1,5), '1-5'),
    ((6,10), '6-10'),
    ((11, 20), '11-20'),
    ((21,1000), '20+'),
)

class Att(django_filters.FilterSet):
    #q1=AttributeChoiceValue.objects.filter(attribute__name='price')
    #q2=AttributeChoiceValue.objects.filter(attribute__name='duration')
    #q3=AttributeChoiceValue.objects.filter(attribute__name='number_of_people')
    q1=AttributeChoiceValue.objects.filter(attribute__name='tour_type')
    q2=AttributeChoiceValue.objects.filter(attribute__name='activity')
    q3=AttributeChoiceValue.objects.filter(attribute__name='nature_of_trips')

    # price=(django_filters.ModelMultipleChoiceFilter(
    #     queryset=q1.values_list('name', flat=True).distinct(),
    #     widget=forms.CheckboxSelectMultiple))


    # duration=(django_filters.ModelMultipleChoiceFilter(
    #     queryset=q2.values_list('name', flat=True).distinct(),
    #     widget=forms.CheckboxSelectMultiple))

    number_of_people = django_filters.MultipleChoiceFilter(field_name='number_of_people', choices=people,widget=forms.CheckboxSelectMultiple)

    tour_type=(django_filters.ModelMultipleChoiceFilter(
        queryset=q1.values_list('name', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple))

    activity=(django_filters.ModelMultipleChoiceFilter(
        queryset=q2.values_list('name', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple))

    nature_of_trips=(django_filters.ModelMultipleChoiceFilter(
        queryset=q3.values_list('name', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple))

    price = django_filters.MultipleChoiceFilter(field_name='price',choices=price,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model=AttributeChoiceValue
        fields=()
