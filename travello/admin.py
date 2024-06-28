from django.contrib import admin
from .models import  Destination , Gallery ,CustomTags

# Register your models here.
admin.site.register(Destination)
admin.site.register(Gallery)
admin.site.register(CustomTags)
