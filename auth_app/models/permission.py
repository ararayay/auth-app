from django.db import models


class Permission(models.Model):
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=50)

    class Meta:
        unique_together = ('resource', 'action')
        verbose_name = 'Разрешение'
        verbose_name_plural = 'Разрешения'

    def __str__(self):
        return f'{self.resource}:{self.action}'
