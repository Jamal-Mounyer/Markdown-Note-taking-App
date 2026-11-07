from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    md_note = models.FileField(upload_to='notes/', null=False, blank=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
        null=False,
        blank=False
    )