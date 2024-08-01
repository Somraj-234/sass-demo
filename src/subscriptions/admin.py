from django.contrib import admin

# Register your models here.
from .models import Subscriptions, UserSubscription

admin.site.register(Subscriptions)

admin.site.register(UserSubscription)
