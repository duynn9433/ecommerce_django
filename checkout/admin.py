from django.contrib import admin

from checkout.models import OrderItem, Order


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'status', 'transaction_id', 'user')
    list_filter = ('status', 'date')
    search_fields = ('email', 'shipping_name', 'id', 'transaction_id')
    inlines = [OrderItemInline, ]

    fieldsets = (
        ('Basics', {'fields': ('status', 'email', 'phone')}),
        ('Shipping', {'fields': ('shipping_name', 'shipping_address_1',
                                 'shipping_address_2', 'shipping_city', 'shipping_state',
                                 'shipping_zip', 'shipping_country')})
    )


admin.site.register(Order, OrderAdmin)

