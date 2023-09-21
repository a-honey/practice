from django.core.files.base import ContentFile
from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)

    def save_image_from_bytes(self, image_data, image_name):
        self.image.save(image_name, ContentFile(image_data), save=False)
        self.save()

    def get_image_url(self):
        return self.image.url
