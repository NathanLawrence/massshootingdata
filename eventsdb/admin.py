from django.contrib import admin
from eventsdb.models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Article)
admin.site.register(Shooter)
admin.site.register(Weapon)