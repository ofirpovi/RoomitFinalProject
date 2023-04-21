from django.contrib import admin

# Register your models here.
from .models import Scores, RequirementsR, RequirementsP, Offers
admin.site.register(Scores)
admin.site.register(RequirementsR)
admin.site.register(RequirementsP)
admin.site.register(Offers)
