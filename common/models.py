from django.db import models
class BaseModel(models.Model):
    """
    An abstract base model that provides common fields for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        ordering = ['-created_at']  # Default ordering by creation time
        verbose_name = "Base Model"
        verbose_name_plural = "Base Models"