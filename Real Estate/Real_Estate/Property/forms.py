from django.forms import ModelForm
from .models import Properties


class PropertyForm(ModelForm):
    class Meta:
        model = Properties
        fields = ['property_title', 'property_address', 'property_city', 'property_state', 'property_pin',
                  'property_price', 'property_bedroom', 'property_bathroom', 'property_sq_feet', 'property_lot_size',
                  'property_garage', 'property_description', 'property_image1', 'property_image2', 'property_image3',
                  'property_image4', 'property_image5']
