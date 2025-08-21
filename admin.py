from django.contrib import admin
from .models import ItemsList, Items, AboutUs, Feedback, BookTable

# Register your models here
admin.site.register(ItemsList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(BookTable)
