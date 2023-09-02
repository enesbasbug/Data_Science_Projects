from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    gptkey = models.CharField(max_length=255, default=settings.GPT_KEY)
    is_paid_std = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_paid_ult = models.BooleanField(default=False)
    username = None
    paid_date = models.DateTimeField(null=True, blank=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def update_paid_status(self):
        now = timezone.now()

        if self.is_paid_ult:  # If it's an annual membership
            payment_expiry_date = self.paid_date + timezone.timedelta(days=365) if self.paid_date else None
            # payment_expiry_date = self.paid_date + timezone.timedelta(minutes=2) if self.paid_date else None
        else:  # For other monthly membership types
            payment_expiry_date = self.paid_date + timezone.timedelta(days=30) if self.paid_date else None
            # payment_expiry_date = self.paid_date + timezone.timedelta(minutes=2) if self.paid_date else None

        if payment_expiry_date and payment_expiry_date <= now:
            self.is_paid_std = False
            self.is_paid = False
            self.is_paid_ult = False
            self.paid_date = None
            self.save()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.email} - {self.payment_date}"
