from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(TranslatePage)
class Malumot(TranslationOptions):
    fields = ('slider_title', 'title', 'aboute')