from django.contrib import admin

# Register your models here.
from order.models import Order, OrderDetail, ShopCart


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'total', 'status', 'note', 'create_at')
    list_filter = ('create_at', 'status')
    readonly_fields = ('user', 'name', 'surname', 'address', 'city', 'phone', 'total')


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'user', 'total', 'create_at')
    list_filter = ('create_at',)

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
