from django.contrib import admin
from .models import Tutorial 
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item
from .models import Pictures
from .models import BookSeat
# Register your models here.
admin.site.register(Tutorial)  # Here 'Tutorial' is the model name

admin.site.register(Pictures)  # Here 'Pictures' is the model name

admin.site.register(BookSeat) 

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
