from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total when lineitems are updated/created
    """
    instance.order.update_total()


def update_on_delete(sender, instance, **kwargs):
    """
    Update order total when lineitems are deleted
    """
    instance.order.update_total()
