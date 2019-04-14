from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile


class Properties(models.Model):
    property_seller_name = models.ForeignKey(User, on_delete=models.CASCADE)
    property_title = models.CharField(max_length=100, blank=False, unique=True)
    property_address = models.CharField(max_length=100, blank=False)
    property_city_choices = (
        ('Ghaziabad', 'Ghaziabad'),
        ('New Delhi', 'New Delhi'),
        ('Gurugram', 'Gurugram'),
        ('Chandigarh', 'Chandigarh'),
        ('Bangalore', 'Bangalore'),
    )
    property_city = models.CharField(max_length=100, choices=property_city_choices)
    property_state_choices = (
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Delhi', 'Delhi'),
        ('Haryana', 'Haryana'),
        ('Punjab', 'Punjab'),
        ('Karnataka', 'Karnataka'),
    )
    property_state = models.CharField(max_length=100, choices=property_state_choices)
    property_pin = models.IntegerField(blank=False)
    property_price = models.IntegerField(blank=False)
    property_bedroom = models.IntegerField(default=1)
    property_bathroom = models.IntegerField(default=1)
    property_sq_feet = models.IntegerField(blank=False)
    property_lot_size = models.IntegerField(blank=False)
    property_garage = models.IntegerField(default=0)
    property_listing_date = models.DateField(auto_now_add=True)
    property_description = models.CharField(max_length=500)
    property_image1 = models.ImageField(upload_to='media/property', blank=False,
                                        default="property/default_property.jpg")
    property_image2 = models.ImageField(upload_to='media/property', default="property/default_property.jpg", blank=True)
    property_image3 = models.ImageField(upload_to='media/property', default="property/default_property.jpg", blank=True)
    property_image4 = models.ImageField(upload_to='media/property', default="property/default_property.jpg", blank=True)
    property_image5 = models.ImageField(upload_to='media/property', default="property/default_property.jpg", blank=True)

    def __str__(self):
        return self.property_seller_name.first_name


class Enquiry(models.Model):
    enquiry_user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.enquiry_user.email
