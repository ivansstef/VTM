# **Copilot_Plan_VTM.md**

Повна інструкція для GitHub Copilot / Assistant із покроковою технічною логікою реалізації проєкту **VTM (Vehicle & Technical Material Management System)**.

> ⚠️ **DO NOT EXECUTE COMMANDS AUTOMATICALLY.**  
> Усі дії виконуються під контролем користувача вручну.

---

## **01 – Project Structure Overview**
**Мета:** Ознайомити Copilot із файловою структурою проєкту та базовими правилами розміщення.

### Дії:
1. Прочитати наявну файлову структуру.
2. Взяти за базу наступну архітектуру:
```
VTM/
├── app/
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│   ├── reports.py
│   └── utils/
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── icons/
├── backup/
├── doc/
│   ├── VTM_Master_Summary.md
│   ├── VTM_Future_Features_Roadmap.md
│   └── README.md
├── config.ini
├── requirements.txt
├── .gitignore
└── main.py
```
3. Не змінювати папки `/doc/`, `/backup/`, `/static/`.
4. Головний застосунок — Flask, точка входу: `main.py`.

### Результат:
- Оновлена структура з перевіркою наявності всіх директорій.
- Коментар Copilot у логі: *“Structure confirmed. Proceeding to documentation parsing.”*

---

## **02 – Documentation Reading**
**Мета:** Ознайомити Copilot із технічною базою VTM.

### Дії:
1. Прочитати всі `.md` файли з `/doc/`.
2. Головні документи для контексту:  
   - `VTM_Master_Summary.md` (архітектура, база даних, логіка)  
   - `VTM_Future_Features_Roadmap.md` (план спринтів)
3. Зробити короткий технічний конспект (до 30 рядків).

### Результат:
- Copilot «входить у курс справи» і зберігає контекст для наступних кроків.

---

## **03 – Implementation Plan**
**Мета:** Сформувати покроковий технічний план реалізації MVP.

### Дії:
1. Створити файл `Implementation_Plan.md` у `/doc/`.
2. Розділи:
   - Environment setup
   - Database creation (SQLite)
   - Flask app skeleton
   - Templates/UI integration
   - Reports generation
   - Backup system
   - Roles/authentication
   - Testing & packaging
3. Кожен розділ = майбутній коміт.

### Результат:
- Файл `Implementation_Plan.md` зі структурою майбутньої роботи.

---

## **04 – Stage Prompts**
**Мета:** Створити внутрішні технічні промпти для кожного етапу розробки.

### Дії:
1. Створити в `/prompts/` файли:
```
stage1_database.md
stage2_flask_app.md
stage3_templates.md
stage4_reports.md
stage5_backup_roles.md
stage6_testing_packaging.md
```
2. У кожному описати:
   - мету етапу;
   - необхідні дії;
   - очікувані файли/зміни;
   - коментар Copilot для завершення етапу.

### Результат:
- 6 окремих stage-файлів готові для виконання Copilot'ом послідовно.

---

## **05 – Environment Check & Setup**
**Мета:** Перевірити середовище розробки, залежності та сумісність.

### Дії:
1. Переконатись, що в системі є Python ≥ 3.12.
2. Створити або активувати `venv`.
3. Перевірити пакети:
   - flask
   - sqlite3
   - reportlab
   - openpyxl
   - bcrypt
   - requests
4. Якщо щось відсутнє — додати до `requirements.txt`.

### Результат:
- Оновлений `requirements.txt`.
- Коментар Copilot: *“Environment verified and all dependencies are listed.”*

---

## **06 – Gitignore & Requirements**
**Мета:** Створити `.gitignore` та фіналізувати `requirements.txt`.

### Дії:
1. `.gitignore` має виключати:
```
/venv/
/__pycache__/
/backup/
/instance/
/uploads/
*.db
```
2. `requirements.txt` — один рядок на пакет.
3. Перевірити відповідність середовища.

### Результат:
- `.gitignore` і `requirements.txt` готові.

---

## **07 – GitHub Upload Preparation**
**Мета:** Підготувати структуру до завантаження в GitHub.

### Дії:
1. Створити локальний git-репозиторій.
2. Згенерувати послідовність команд для користувача:
```
git init
git add .
git commit -m "Initial VTM MVP commit"
git branch -M main
git remote add origin <repo_url>
git push -u origin main
```
3. Не виконувати ці команди автоматично.

### Результат:
- Інструкція готова.
- Copilot додає її в `Upload_Instructions.md`.

---

## **08 – Commits & Documentation**
**Мета:** Формалізувати коміти, опис і документацію.

### Дії:
1. Після кожного етапу створювати коміт виду:
   - `#stage1_database_created`
   - `#stage2_flask_initialized`
   - ...
2. Створити:
   - `README.md` (короткий опис проєкту)
   - `User_Guide.md` (інструкція користувача)
   - `Changelog.md` (зміни)
   - `Testing_Log.md` (журнал тестів)

### Результат:
- Повний набір документації в `/doc/`.

---

## **09 – Testing Scripts**
**Мета:** Додати базове автоматичне тестування.

### Дії:
1. Створити тести для ключових модулів:
```
test_database.py
test_flask_app.py
test_reports.py
```
2. Виконати базові юніт-тести (pytest або unittest).
3. Лог зберігати у `/tests/logs/`.

### Результат:
- Наявність тестів, що перевіряють коректність базових функцій.

---

## **10 – Packaging & Android Compatibility**
**Мета:** Підготувати застосунок до майбутньої збірки в APK.

### Дії:
1. Перевірити, що структура сумісна з BeeWare (Briefcase).
2. Створити `beeware_config.json` із базовими параметрами.
3. Перевірити імпорти — не має бути системних залежностей.
4. Додати до плану майбутню команду:
```
briefcase create android
briefcase build android
```
(але не виконувати її зараз)

### Результат:
- Проєкт готовий до подальшої збірки під Android.

---

> ✅ **Copilot_Plan_VTM.md** — центральний план інтеграції Copilot у технічний процес проєкту VTM.  
> Використовується як головний файл запуску для поступової автоматизації, тестування та публікації.

