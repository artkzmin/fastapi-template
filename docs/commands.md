# Полезные команды для разработки

## Оглавление
- [Ruff](#ruff)
- [Alembic](#alembic)

## Ruff
Линтер:
```bash
ruff check
```
Форматирование:
```bash
ruff format
```

## Alembic
Создание ревизии:
```bash
alembic revision --autogenerate -m "comment"
```
Применение миграций:
```bash
alembic upgrade head
```