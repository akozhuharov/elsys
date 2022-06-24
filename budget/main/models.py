from django.db import models


TRANSACTION_CHOISES = (
    ("IN", "Income"),
    ("OUT", "Out")
)


class Transaction(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=3, choices=TRANSACTION_CHOISES)