from django.contrib import admin
from .models import Profile , PropertyForOffer, Image
from roomit_app.models import Scores, RequirementsR, RequirementsP, Offers
# Register your models here.
admin.site.register(Profile)
admin.site.register(PropertyForOffer)
admin.site.register(Image)
admin.site.register(Scores)
admin.site.register(RequirementsR)
admin.site.register(RequirementsP)
admin.site.register(Offers)

