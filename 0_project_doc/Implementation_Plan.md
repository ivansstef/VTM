# **VTM Implementation Plan**

## 📋 Overview
План поетапної реалізації системи обліку військово-технічного майна (VTM) з детальними кроками, критеріями валідації та очікуваними результатами.

## 1️⃣ Environment Setup

### 1.1. Python Configuration
```bash
# Python 3.12 або вище
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

### 1.2. Dependencies Installation
```txt
# requirements.txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-Migrate==4.0.5
python-dotenv==1.0.0
reportlab==4.0.7
openpyxl==3.1.2
```

### 1.3. Development Tools
- VS Code з розширеннями:
  - Python
  - SQLite Viewer
  - Git Graph
- SQLite Browser для роботи з БД
- Git для версіонування

### ✅ Validation Criteria
- [ ] `python --version` показує 3.12+
- [ ] Всі залежності встановлені
- [ ] Flask запускається без помилок

## 2️⃣ Database Implementation

### 2.1. SQLite Schema
```sql
-- Core Tables
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_type TEXT NOT NULL,
    doc_number TEXT NOT NULL,
    doc_date DATE NOT NULL,
    service_id INTEGER,
    supplier_id INTEGER,
    created_by INTEGER,
    is_locked BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE document_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER,
    item_name TEXT NOT NULL,
    item_code TEXT,
    unit TEXT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    category INTEGER CHECK(category BETWEEN 1 AND 5),
    note TEXT
);

CREATE TABLE stock_balance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    service_id INTEGER,
    category INTEGER,
    quantity DECIMAL(10,2) DEFAULT 0,
    last_update TIMESTAMP
);
```

### 2.2. Models Definition
```python
# models.py
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_type = db.Column(db.String(20), nullable=False)
    items = db.relationship('DocumentItem', backref='document', lazy=True)

class StockBalance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Numeric(10,2), default=0)
```

### 2.3. Migration Setup
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### ✅ Validation Criteria
- [ ] Всі таблиці створені
- [ ] Зв'язки працюють коректно
- [ ] Міграції виконуються без помилок

## 3️⃣ Flask Application Structure

### 3.1. Core Structure
```
app/
├── __init__.py      # Flask app initialization
├── routes.py        # URL routes
├── models.py        # Database models
├── forms.py         # WTForms classes
└── utils.py         # Helper functions
```

### 3.2. Configuration
```python
# config.py
class Config:
    SECRET_KEY = 'dev-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vtm.db'
    BACKUP_PATH = 'backup/'
```

### ✅ Validation Criteria
- [ ] Flask запускається
- [ ] Роути відповідають
- [ ] Конфігурація завантажується

## 4️⃣ Templates & UI

### 4.1. Base Templates
```
templates/
├── base.html           # Base template
├── auth/
│   ├── login.html
│   └── register.html
├── documents/
│   ├── create.html
│   └── list.html
└── reports/
    └── generate.html
```

### 4.2. Static Assets
```
static/
├── css/
│   └── style.css
├── js/
│   └── main.js
└── img/
```

### ✅ Validation Criteria
- [ ] Шаблони рендеряться
- [ ] Стилі застосовуються
- [ ] JavaScript працює

## 5️⃣ Features Implementation

### 5.1. Authentication
- Login/Logout функціонал
- Ролі користувачів
- Захист роутів

### 5.2. Document Management
- Створення документів
- Валідація даних
- Оновлення залишків

### 5.3. Report Generation
- PDF звіти
- Excel експорт
- Фільтрація даних

### ✅ Validation Criteria
- [ ] Авторизація працює
- [ ] Документи зберігаються
- [ ] Звіти генеруються

## 6️⃣ Testing & Deployment

### 6.1. Testing
```python
# test_documents.py
def test_create_document():
    doc = Document(doc_type='прихід')
    assert doc.doc_type == 'прихід'
```

### 6.2. Deployment Steps
1. Налаштування production config
2. Створення системного сервісу
3. Налаштування backup

### ✅ Validation Criteria
- [ ] Всі тести проходять
- [ ] Система працює в production
- [ ] Бекапи створюються

## 📊 Progress Tracking

### Milestone 1: Basic Setup
- [x] Project structure
- [x] Environment setup
- [ ] Database schema

### Milestone 2: Core Features
- [ ] Authentication
- [ ] Document management
- [ ] Basic reports

### Milestone 3: Advanced Features
- [ ] Advanced reports
- [ ] Backup system
- [ ] User management

## 🔄 Iteration Plan

1. **Week 1:** Environment & Database
2. **Week 2:** Core Features
3. **Week 3:** UI & Reports
4. **Week 4:** Testing & Documentation

## 📝 Notes

- Регулярно комітити зміни
- Документувати всі рішення
- Тестувати кожну функцію
- Перевіряти офлайн-режим
