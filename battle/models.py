from django.db import models
from super_types.models import Super_Types
from super.models import Super

# Create your models here.
class Battle(models.Model):
    super_one = models.ForeignKey(Super_Types, on_delete=models.CASCADE)
    super_two = models.ForeignKey(Super, on_delete=models.CASCADE)
    battle_date = models.DateTimeField(auto_now=False, auto_now_add=False)