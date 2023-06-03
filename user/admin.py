from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Project)


