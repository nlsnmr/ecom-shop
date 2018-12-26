from django.db import models
from django.db.models.signals import pre_save

from carts.models import Cart
from ecommerce.utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
    ('canceled', 'Canceled'),
)


class Order(models.Model):
    # billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True)
    order_id = models.CharField(max_length=120, blank=True)
    # shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True)
    # billing_address     = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True)
    shipping_address_final = models.TextField(blank=True, null=True)
    billing_address_final = models.TextField(blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=False)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    # qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    # if qs.exists():
    #     qs.update(active=False)
    #
    # if instance.shipping_address and not instance.shipping_address_final:
    #     instance.shipping_address_final = instance.shipping_address.get_address()
    #
    # if instance.billing_address and not instance.billing_address_final:
    #     instance.billing_address_final = instance.billing_address.get_address()


pre_save.connect(pre_save_create_order_id, sender=Order)