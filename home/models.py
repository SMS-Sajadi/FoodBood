from django.db import models
from accounts.models import UserTable


class Address(models.Model):
    """
    This is the Model for saving addresses in a user profile
    """
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name='fav_addr')
    address = models.CharField(max_length=500, null=False, blank=False, default='Isfahan')

    class Meta:
        unique_together = ['user', 'address']

    def __str__(self):
        return self.address
