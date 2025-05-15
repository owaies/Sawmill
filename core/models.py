from django.db import models

class SiteContent(models.Model):
    SECTION_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('products', 'Products'),
        ('gallery', 'Gallery'),
        ('contact', 'Contact'),
    ]
    CONTENT_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('color', 'Color'),
        ('map', 'Map'),
    ]

    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    key = models.CharField(max_length=100)  # e.g. heroText
    value = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    map_url = models.URLField(blank=True, null=True)  # Field for storing map URL

    def __str__(self):
        return f"{self.section} - {self.key}"
class BackgroundImage(models.Model):
    section = models.CharField(max_length=20, choices=[
        ('navbar', 'Navbar'),
        ('home', 'Home'),
        ('about', 'About'),
        ('gallery', 'Gallery'),
        ('products', 'Products'),
        ('contact', 'Contact'),
        ('footer', 'Footer'),
    ])
    image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.section
