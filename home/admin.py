from django.contrib import admin
from home.models import services, toPricing, portfolio, staff, prices, carousel

# Register your models here.

admin.site.register(services)
admin.site.register(toPricing)
admin.site.register(portfolio)
admin.site.register(staff)
admin.site.register(prices)
admin.site.register(carousel)