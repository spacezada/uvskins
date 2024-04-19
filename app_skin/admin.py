from django.contrib import admin
from .models import Skin

class SkinsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Skin)

