from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import *

class ProfileAdmin(SnippetViewSet):
    model = Profile
    menu_label = "Profile Admin"
    icon = "tag"
    menu_order = 18
    list_display = (
        "user",
        "created",
    )
    search_field = ("user",)
    
register_snippet(ProfileAdmin)