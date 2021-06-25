from django.contrib import admin
# точка означает поиск модуля в одном каталоге с admin.py
from .models import Topic, Entry
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
