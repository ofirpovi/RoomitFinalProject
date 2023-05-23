import django_filters
from users.models import PropertyForOffer, Profile

class PropertyOfferFilter(django_filters.FilterSet):
    rent = django_filters.RangeFilter()
    square_meters = django_filters.RangeFilter()
    rooms_number = django_filters.RangeFilter()
    renovated = django_filters.BooleanFilter()
    shelter_inside = django_filters.BooleanFilter()
    shelter_nearby = django_filters.BooleanFilter()
    furnished = django_filters.BooleanFilter()
    shared_livingroom = django_filters.BooleanFilter()

    class Meta:
        model = PropertyForOffer
        fields = {
            'rent': ['exact'],
            'square_meters': ['exact'],
            'rooms_number': ['exact'],
            'renovated': ['exact'],
            'shelter_inside': ['exact'], 
            'shelter_nearby': ['exact'], 
            'furnished': ['exact'], 
            'shared_livingroom': ['exact']
        }


class RoommateFilter(django_filters.FilterSet):
        smoker = django_filters.BooleanFilter()
        kosher = django_filters.BooleanFilter()
    
        class Meta:
            model = Profile
            fields = {
                'gender': ['exact'], 
                'occupation': ['exact'],
                'diet' : ['exact'],
                'status': ['exact'],
                'hospitality': ['exact'],
                'smoker' : ['exact'],
                'kosher' : ['exact'],
            }

    