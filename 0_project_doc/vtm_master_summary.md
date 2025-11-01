# **VTM – Master Summary (Technical Specification)**

---

## 1. **Project Scope & Principles**
**Name:** VTM (Vehicle & Technical Material Management System)  
**Version:** MVP 1.0  
**Status:** Offline-first, single-user prototype with admin/user roles.

**Purpose:**  
To automate the accounting of military-technical property (ВТМ), replacing paper-based records with a local digital tool capable of generating official reports, maintaining inventory, and ensuring offline reliability.

**Core Principles:**
- Offline-first, no dependency on internet or GSM.
- SQLite as the primary local database.
- Universal document form (Прихід / Розхід) as the main operational entity.
- Direct mapping to existing military accounting standards (Наказ №440, дод.32, форми 1–2).
- Modular architecture, expandable via REST API for future sync.

---

## 2. **Data Model (MVP)**

### 2.1 Main Tables
| Table | Description | Key Fields |
|--------|--------------|-------------|
| **documents** | Header of every document (прихід/розхід) | id (UUID), doc_type, doc_name, doc_number, doc_date, service_id, supplier_id, created_by, is_locked, created_at |
| **document_items** | Line items of a document | id, document_id (FK), item_name, item_code, unit, quantity, category, note |
| **stock_balance** | Current stock levels | id, item_name, service_id, category, quantity, last_update |
| **services** | Reference list of services | id, name, code |
| **suppliers** | Providers/receivers of items | id, name, type |
| **users** | Local users (admin/user) | id, username, password_hash, role, created_at |
| **chiefs** | Heads of services for signature logic | id, service_id, rank, initials, surname, period_from, period_to |
| **audit_log** | User action log | id, user_id, action, target_table, record_id, timestamp, note |

### 2.2 Relationships
- `documents.id` → `document_items.document_id`
- `services.id` → `documents.service_id` and `stock_balance.service_id`
- `users.id` → `audit_log.user_id`
- `chiefs.service_id` → `documents.service_id`

### 2.3 Field Conventions
| Field | Rule |
|--------|------|
| `quantity` | numeric(10,2), must be ≥ 0 |
| `category` | integer ∈ [1..5] |
| `doc_number` | pattern: `[служба]-[рік]-[№]` (e.g., АС-25-001) |
| `is_locked` | 0=open / 1=closed |
| `last_update` | ISO timestamp (UTC) |

---

## 3. **Document Flow (Logic & UX)**

### 3.1 Creation Process
1. User opens form → selects **type (прихід / розхід)**.
2. Fills document header (date, number, supplier, service, etc.).
3. Adds line items via **“Add Row”** button or input number of rows.
4. On save → program:
   - validates all fields (not empty, category valid, qty > 0);
   - checks stock (if розхід → ensures enough quantity, else blocks save);
   - updates `stock_balance` (add/subtract accordingly);
   - logs action in `audit_log`.

### 3.2 Editing / Locking
- Documents remain editable until **closed (is_locked=1)**.
- Only **Admin** can lock/unlock documents.
- All changes (edit/delete) logged in `audit_log`.

### 3.3 Duplication
- Button **“Duplicate Document”** copies header and all positions.
- New doc receives new ID and doc_number.

### 3.4 Multi-line Support
- Each document may contain multiple line items with identical item_name but different categories.
- Example: “Свічки автомобільні, код 56 — к-сть 2 (кат.1)” and same name with cat.2.

---

## 4. **Reports (MVP)**

### 4.1 Available Reports
| Report | Filters | Output | Description |
|---------|----------|----------|--------------|
| **Stock on Date (Залишки)** | service, category, subdivision, date | PDF / Excel | Shows current stock at selected date |
| **Movement by Period (Рух)** | service, category, date_from/date_to | PDF / Excel | Displays all incoming/outgoing movements |
| **Documents Journal (Журнал)** | service, date_from/date_to | PDF / Excel | List of documents for reconciliation |
| **Form 1** | service, quarter | PDF | Summary verification report |
| **Form 2** | service, month | PDF | Monthly reconciliation summary |

### 4.2 Generation Rules
- Reports generated dynamically (no caching).
- Form templates conform to Наказ №440 formatting (header, signatures, emblem).
- Export through `ReportLab` (PDF) and `openpyxl` (Excel).

---

## 5. **Security & Roles**

| Role | Access Rights |
|-------|----------------|
| **Admin** | full access; edit/delete documents; manage users, services, chiefs; lock/unlock; run backups |
| **User** | create/edit documents; generate reports; cannot delete or unlock |

### Authentication
- Local login (username/password).
- Passwords stored as hashed (bcrypt/sha256).

### Audit Logging
- All critical actions logged: create/edit/delete document, login, backup, sync.
- Log fields: timestamp, user, action, object, comment.

---

## 6. **Backup & Recovery**

### 6.1 Policy
| Type | Trigger | Destination |
|-------|----------|--------------|
| **Auto Backup** | Every Sunday 21:00 | `/backup/yyyy-mm-dd.db` |
| **Manual Backup** | Button in Admin panel | `/backup/manual_<timestamp>.db` |

### 6.2 Recovery
- Admin can restore from selected backup.
- Backup structure identical to `main.db`.

---

## 7. **Future Integration Plan (Reference)**
*(based on VTM – Future Features & Sprint Roadmap)*

| Sprint | Planned Feature | Description |
|---------|----------------|--------------|
| **2** | REST API & Sync | Two-way data sync between local (SQLite) and central (PostgreSQL) via Flask API. Conflict rule: `last-modified-wins`. |
| **3** | Multiuser & Tokens | Role-based tokens, remote logins, centralized `audit_log`. |
| **4** | OCR & Automation | Auto-fill of document fields using Tesseract OCR. |
| **5** | Analytics & Advanced Reports | Data visualization, expanded Excel exports. |
| **6** | UX Polish & Mobile APK | Final BeeWare build for Android, full offline operation. |

---

## 8. **Appendices**

### A. **Chiefs Directory Logic**
- Each `chief` record active if document.date ∈ [period_from, period_to].
- Signature auto-fills in reports using rank + initials + surname.
- TBD: initials generation format (e.g., І.П. Прізвище).

### B. **Excel Utilities**
- Power Query templates for external reconciliation with financial part.
- VBA macro: auto column width adjustment (Журнал документів, Журнал найменувань).

### C. **OCR Target Fields (for Sprint 4)**
- Recognized fields: doc_date, doc_number, item_name, quantity, category, supplier.
- Supported format: scanned PDF / photo.
- Language: Ukrainian (Tesseract + LangData).

### D. **Normative Base (Reference)**
| Document | Description |
|-----------|--------------|
| **Наказ МОУ №440** | Порядок ведення обліку військово-технічного майна. |
| **Додаток 32** | Картка обліку матеріальних засобів (службова форма). |
| **Додатки 1–2** | Форми звірок і інвентаризаційних звітів. |
| **Вимоги ЗСУ до звітності PDF/Excel** | Основні реквізити шапки, герб, підписи. |

---

> ✅ **Document Purpose:** consolidated technical summary of VTM project (MVP + roadmap).
> Use this file as the master reference for architecture, logic, and data model.
> All future enhancements must refer to section 7 before modification.

