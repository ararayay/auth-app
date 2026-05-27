# auth-app

Тестовое задание для Effective Mobile.

## Описание проекта

Backend-приложение реализует собственную систему аутентификации и авторизации на базе Django REST Framework и JWT. Основная задача проекта - продемонстрировать реализацию:
- регистрации и аутентификации пользователей;
- собственной RBAC-архитектуры (Role-Based Access Control);
- проверки доступа к ресурсам приложения.

Документация Swagger доступна по адресу:

```text
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## Используемые технологии

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)

---

## Authentication

Для аутентификации используется JWT.

После успешного login пользователь получает:

```json
{
  "access": "...",
  "refresh": "..."
}
```

---

## Logout

При logout: refresh token добавляется в blacklist.

---

## Soft Delete пользователя

Удаление пользователя реализовано через soft delete.

При удалении:
- пользователь получает logout;
- поле `is_active=False`;
- вход в систему становится невозможен;
- запись в БД сохраняется.

---

## Authorization System

В проекте реализована собственная RBAC-система (Role-Based Access Control). Права доступа определяются ролями пользователя. Основные сущности:

- User - пользователь системы
- Role - роль пользователя 
- Permission - разрешение на выполнение действия над ресурсом;
- UserRole - связь пользователя и роли; 
- RolePermission - связь роли и разрешения.
 
Схема проверки доступа:

```text
User -> Role -> Permission -> Resource + Action
```

В проекте используются mock бизнес-ресурсы: Projects и Reports. Есть 3 роли:
1. Employee - работает с отчетами, не имеет доступа к управлению проектами: reports:create, reports:read 
2. Manager - работает с проектами: projects:create, projects:read 
3. Admin - администратор системы, может управлять ролями, назначать permissions, назначать роли пользователям.

Созданы тестовые пользователи:
1. Admin

email: example@gmail.com  
password: admin123

2. Manager

email: user@example3.com  
password: petrpetrov

3. Employee

email: user@example2.com 
password: ivanivanov
---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register/` | Регистрация |
| POST | `/login/` | Вход |
| POST | `/logout/` | Выход |
| GET | `/user/` | Информация о пользователе |
| PATCH | `/user/` | Обновление профиля |
| DELETE | `/user/` | Soft delete пользователя |

---

## Mock Resources

| Method | Endpoint | Permission |
|---|---|---|
| GET | `/projects/` | projects:read |
| POST | `/projects/` | projects:create |
| GET | `/reports/` | reports:read |
| POST | `/reports/` | reports:create |

---

## Запуск проекта

Чтобы запустить проект, нужно:
1. Установить зависимости

```bash
pip install -r requirements.txt
```

2. Применить миграций

```bash
python manage.py migrate
```

3. Запустить сервер

```bash
python manage.py runserver
```

4. Загрузить тестовые данные

```bash
python manage.py loaddata auth_app/fixtures/initial_data.json
