from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    
    
    class Meta():
        abstract = True
        
        
class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    
    def isNegative(self):
        return self.amount < 0
    
    class Meta():
        ordering = ['description']
