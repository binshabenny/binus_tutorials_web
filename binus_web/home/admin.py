from django.contrib import admin
from .models import Tutorial 
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

# Register your models here.
admin.site.register(Tutorial)  # Here 'Tutorial' is the model name


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
