from django import forms
from real_estate.models import RealEstate, DealRequest, Photo


class RealEstateForm(forms.ModelForm):
    class Meta:
        model = RealEstate
        fields = ['city_district', 'metro', 'street', 'building_number', 'floors_in_house', 'floor',
                  'rooms', 'area_of_premise', 'type_of_deal', 'bathroom', 'balcony', 'title_photo']


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        fields = ['suggest_text', ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', ]
