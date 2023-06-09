from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(AddEducation)
admin.site.register(AddSkills)
admin.site.register(AddExperience)
admin.site.register(AddProject)


