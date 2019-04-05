from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    phone_number = models.IntegerField(null=False, default=0)
    is_seller = models.BooleanField(null=False, default=False)
    is_buyer = models.BooleanField(null=False, default=True)
    image = models.ImageField(default="default.png", upload_to='profile_pics')

    def __str__(self):
        return self.user.first_name

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
        img.save(self.image.path)
