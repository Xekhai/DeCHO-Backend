from django.contrib import admin
from .models import Cause, Giveaway, Wallet, Donation, Approval


# Register your models here.
admin.site.register(Cause)
admin.site.register(Approval)
admin.site.register(Wallet)
admin.site.register(Donation)
admin.site.register(Giveaway)