from django.contrib import admin
from .models import Account,Restaurant,Order,Food,Evaluation,OrderandFood
# Register your models here.
admin.site.register(Account)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Food)
admin.site.register(Evaluation)
admin.site.register(OrderandFood)
