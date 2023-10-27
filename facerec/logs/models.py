from django.db import models
from profiles.models import Profile
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

class Log(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
  photo = models.ImageField(upload_to='logs')
  is_correct = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  
  panels = [
    FieldPanel('profile'),
    FieldPanel('photo'),
    FieldPanel('is_correct'),
  ]
  
  def __str__(self):
    return str(self.id)
  