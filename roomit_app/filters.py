import django_filters
from users.models import PropertyForOffer, Profile
from django_filters import rest_framework as filters
from datetime import datetime, timedelta
from decimal import Decimal


class PropertyOfferFilter(django_filters.FilterSet):
    rent = django_filters.RangeFilter()
    square_meters = django_filters.RangeFilter()
    rooms_number = django_filters.RangeFilter()
    roomates_number = django_filters.RangeFilter()
    toilets_number = django_filters.RangeFilter()
    renovated = django_filters.BooleanFilter()
    shelter_inside = django_filters.BooleanFilter()
    shelter_nearby = django_filters.BooleanFilter()
    furnished = django_filters.BooleanFilter()
    shared_livingroom = django_filters.BooleanFilter()

    class Meta:
        model = PropertyForOffer
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'neighborhood': ['exact'],
            'rent': ['exact'],
            'square_meters': ['exact'],
            'rooms_number': ['exact'],
            'roomates_number': ['exact'],
            'toilets_number': ['exact'],
            'renovated': ['exact'],
            'shelter_inside': ['exact'],
            'shelter_nearby': ['exact'],
            'furnished': ['exact'],
            'shared_livingroom': ['exact']
        }


class RoommateFilter(django_filters.FilterSet):
    smoker = django_filters.BooleanFilter()
    kosher = django_filters.BooleanFilter()
    expense_management = django_filters.ChoiceFilter()
    min_age = filters.NumberFilter(field_name='birthdate', method='filter_min_age', label='Minimum Age')
    max_age = filters.NumberFilter(field_name='birthdate', method='filter_max_age', label='Maximum Age')
   

    def filter_min_age(self, queryset, name, value):
        today = datetime.now().date()
        min_birthdate = today - timedelta(days=int(Decimal(str(value)))*365)
        return queryset.filter(birthdate__lte=min_birthdate)

    def filter_max_age(self, queryset, name, value):
        today = datetime.now().date()
        max_birthdate = today - timedelta(days=int(Decimal(str(value)))*365)
        return queryset.filter(birthdate__gte=max_birthdate)

    class Meta:
        model = Profile
        fields = {
            'gender': ['exact'],
            'occupation': ['exact'],
            'diet': ['exact'],
            'status': ['exact'],
            'hospitality': ['exact'],
            'smoker': ['exact'],
            'kosher': ['exact'],
            'expense_management': ['exact'],
        }
