from django.contrib import admin
from .models import UserDetails, CardDetails, OrderDetails

admin.site.register(UserDetails)
admin.site.register(CardDetails)
admin.site.register(OrderDetails)

