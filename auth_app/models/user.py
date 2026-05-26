import re, uuid
from transliterate import translit

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    second_name = models.CharField(max_length = 50, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    class Admin(admin.ModelAdmin):
        list_display = ('last_name', 'first_name', 'username', 'email', 'is_active', 'date_joined')
        list_filter = ('is_active',)
        search_fields = ('last_name', 'first_name', 'username', 'email')

    def __str__(self):
        return self.username

    @staticmethod
    def generate_username(first_name: str, last_name: str) -> str:
        """
        Генерирует уникальный username из имени и фамилии. Русские символы транслитерируются.
        Пример: Иван + Петров -> ivan_petrov
        """
        full_name = f"{first_name}_{last_name}".strip().lower()
        username = translit(full_name, 'ru', reversed=True)

        # Проверка уникальности
        while User.objects.filter(username=username).exists():
            suffix = uuid.uuid4().hex[:4]
            username += suffix

        return username

    @classmethod
    def create_user(cls, validated_data: dict) -> AbstractUser:
        """Создаёт пользователя"""
        return super().objects.create_user(
            username=cls.generate_username(validated_data["first_name"], validated_data["last_name"]),
            first_name  =validated_data['first_name'],
            last_name   =validated_data['last_name'],
            email       =validated_data['email'],
            password    =validated_data['password']
        )
