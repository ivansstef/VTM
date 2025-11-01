# Stage 1: Database Implementation Guide

## 🎯 Purpose
Створення та налаштування бази даних SQLite з усіма необхідними таблицями та зв'язками для системи VTM.

## 📋 Steps

### 1. Database Schema Implementation
```python
"""
Task: Create SQLite database schema with tables:
- documents (головна таблиця документів)
- document_items (позиції в документах)
- stock_balance (залишки по службах)
- services (довідник служб)
- suppliers (довідник постачальників/отримувачів)
- users (користувачі системи)
- audit_log (журнал дій)

Ensure proper indexes and foreign keys.
Validate all constraints.
"""
```

### 2. Models Definition
```python
"""
Task: Define SQLAlchemy models for all tables:
- Document class with relationships
- DocumentItem with validations
- StockBalance with quantity checks
- Service and Supplier models
- User model with authentication
- AuditLog for tracking

Include proper relationships and validations.
"""
```

### 3. Migration Setup
```python
"""
Task: Set up database migrations:
- Initialize migration system
- Create initial migration
- Add indexes and constraints
- Implement data seeding
"""
```

## ✅ Expected Results
1. Всі таблиці створені зі зв'язками
2. Моделі реалізовані та протестовані
3. Міграції працюють коректно
4. Базові дані додані

## 🔍 Validation Points
- [ ] `flask db upgrade` виконується без помилок
- [ ] Тестові записи додаються коректно
- [ ] Зв'язки між таблицями працюють
- [ ] Обмеження (constraints) активні
