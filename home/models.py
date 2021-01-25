from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    header = models.CharField(max_length=33, blank=False, default="Home")
    body = models.TextField(max_length=300, blank=True)
    about_text_one = models.TextField(max_length=1000, blank=True)
    about_text_two = models.TextField(max_length=1000, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("header"),
        FieldPanel('body', classname="full"),
        FieldPanel('about_text_one'),
        FieldPanel('about_text_two')
    ]
