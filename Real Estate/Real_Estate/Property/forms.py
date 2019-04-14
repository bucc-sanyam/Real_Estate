from django import forms
from .models import Properties


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['property_title', 'property_address', 'property_city', 'property_state', 'property_pin',
                  'property_price', 'property_bedroom', 'property_bathroom', 'property_sq_feet', 'property_lot_size',
                  'property_garage', 'property_description', 'property_image1', 'property_image2', 'property_image3',
                  'property_image4', 'property_image5']
        labels = {
            'property_title': 'Title',
            'property_address': 'Address',
            'property_city': 'City',
            'property_state': 'State',
            'property_pin': 'PIN Code',
            'property_price': 'Price (INR)',
            'property_bedroom': 'Bedrooms',
            'property_bathroom': 'Bathrooms',
            'property_sq_feet': 'Square Feet',
            'property_lot_size': 'Lot Size',
            'property_garage': 'Garages',
            'property_description': 'Brief Description',
            'property_image1': 'Image 1',
            'property_image2': 'Image 2',
            'property_image3': 'Image 3',
            'property_image4': 'Image 4',
            'property_image5': 'Image 5'
        }
