from django.db import models

from auth_app.models.role import Role
from auth_app.models.permission import Permission


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')
        verbose_name = 'Разрешение роли'
        verbose_name_plural = 'Разрешения ролей'

    def __str__(self):
        return f'{self.role} -> {self.permission}'
