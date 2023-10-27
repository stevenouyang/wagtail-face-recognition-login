from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import *

class LogAdmin(SnippetViewSet):
    model = Log
    menu_label = "Log Admin"
    icon = "tag"
    menu_order = 18
    list_display = (
        "profile",
        "created",
    )
    search_field = ("profile",)
    
register_snippet(LogAdmin)