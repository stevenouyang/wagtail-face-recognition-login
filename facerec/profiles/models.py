from django.db import models
from django.contrib.auth.models import User
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to='photos')
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('user'),
        FieldPanel('photo'),
        FieldPanel('bio'),
    ]

    def __str__(self):
        return f"profile of {self.user.username}"