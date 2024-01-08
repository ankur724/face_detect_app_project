
from django.contrib import admin
from geniusvoice .models import Image
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']


# Register your models here.

