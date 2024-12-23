from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomerUser(AbstractUser):
    store_name = models.CharField(max_length=255, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customeruser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customeruser_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.store_name


class Debt(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="debts")
    customer_name = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    chat_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    duration_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer_name} - {self.amount}"

    def payback(self, amount_paid):
        if self.is_active and amount_paid > 0:
            self.amount -= amount_paid
            if self.amount <= 0:
                self.is_active = False
                self.amount = 0
            self.save()
            return self.amount
        return None


class ReturnDebt(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name="returns")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.debt.payback(self.amount) is not None:
            super().save(*args, **kwargs)
