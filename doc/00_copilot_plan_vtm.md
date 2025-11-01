# **Copilot_Plan_VTM.md (with integrated prompts)**

> ⚠️ **DO NOT EXECUTE COMMANDS AUTOMATICALLY**  
> Усі інструкції нижче призначені для поетапної роботи з GitHub Copilot у Visual Studio Code.

---

## **01 – Project Structure Overview**
**Goal:** Verify and finalize the VTM project folder structure.

**Key actions:**
- Ensure core directories exist
- Create placeholders if missing
- Confirm Flask entry point

### 🧠 PROMPT for Copilot
> **Task:** Analyze and confirm the current VTM project structure.  
> Do not delete, rename, or move any folders.  
> Make sure the following directories exist: `/app`, `/templates`, `/static`, `/backup`, `/doc`.  
> Verify that `/app` contains `routes.py`, `models.py`, `database.py`, and `reports.py`.  
> Confirm that `main.py` is the entry point of the Flask application.  
> If something is missing, generate a minimal placeholder file with a comment header.  
> Finally, print a short summary confirming that the structure is valid.  
> **Do not run or start the app yet.**

*(Пояснення: Copilot перевіряє структуру проєкту, створює відсутні файли й підтверджує готовність.)*

---

## **02 – Documentation Reading**
**Goal:** Load and summarize project documentation.

### 🧠 PROMPT for Copilot
> **Task:** Read all files in the `/doc` directory.  
> Extract and summarize:  
> 1. Technical architecture and components  
> 2. Database schema and relationships  
> 3. MVP features and roadmap  
> 4. Key business rules and constraints  
> Present a concise summary (max 30 lines) focusing on technical implementation details.  
> Do not modify any files.

*(Пояснення: Copilot читає всі документи, створює короткий конспект без змін у файлах.)*

[Продовжити? Це лише початок файлу. Можу надати весь текст, якщо потрібно]# **Copilot_Plan_VTM.md (with integrated prompts)**

> ⚠️ **DO NOT EXECUTE COMMANDS AUTOMATICALLY**  
> Усі інструкції нижче призначені для поетапної роботи з GitHub Copilot у Visual Studio Code.

---

## **01 – Project Structure Overview**
**Goal:** Verify and finalize the VTM project folder structure.

**Key actions:**
- Ensure core directories exist
- Create placeholders if missing
- Confirm Flask entry point

### 🧠 PROMPT for Copilot
> **Task:** Analyze and confirm the current VTM project structure.  
> Do not delete, rename, or move any folders.  
> Make sure the following directories exist: `/app`, `/templates`, `/static`, `/backup`, `/doc`.  
> Verify that `/app` contains `routes.py`, `models.py`, `database.py`, and `reports.py`.  
> Confirm that `main.py` is the entry point of the Flask application.  
> If something is missing, generate a minimal placeholder file with a comment header.  
> Finally, print a short summary confirming that the structure is valid.  
> **Do not run or start the app yet.**

*(Пояснення: Copilot перевіряє структуру проєкту, створює відсутні файли й підтверджує готовність.)*

---

## **02 – Documentation Reading**
**Goal:** Load and summarize project documentation.

### 🧠 PROMPT for Copilot
> **Task:** Read all files in the `/doc` directory.  
> Extract and summarize:  
> 1. Technical architecture and components  
> 2. Database schema and relationships  
> 3. MVP features and roadmap  
> 4. Key business rules and constraints  
> Present a concise summary (max 30 lines) focusing on technical implementation details.  
> Do not modify any files.

*(Пояснення: Copilot читає всі документи, створює короткий конспект без змін у файлах.)*

[Продовжити? Це лише початок файлу. Можу надати
*(Пояснення: Copilot читає всі документи, створює короткий конспект без змін у файлах.)*

---

## **03 – Implementation Plan**
**Goal:** Generate a clear step-by-step development plan for the MVP.

### 🧠 PROMPT for Copilot
> **Task:** Create `/doc/Implementation_Plan.md` containing the sections:  
> Environment setup, Database (SQLite), Flask skeleton, Templates/UI, Reports, Backup, Roles, Testing, Packaging.  
> Each section = one development stage.  
> Output the full markdown file without executing commands.

*(Пояснення: Copilot створює план реалізації — структурований документ для всіх етапів MVP.)*

---

## **04 – Stage Prompts**
**Goal:** Build separate prompts for each development stage.

### 🧠 PROMPT for Copilot
> **Task:** Create a `/prompts/` folder with files:  
> `stage1_database.md`, `stage2_flask_app.md`, `stage3_templates.md`, `stage4_reports.md`, `stage5_backup_roles.md`, `stage6_testing_packaging.md`.  
> In each file, describe purpose, steps, expected results, and closing confirmation message.  
> Do not run code.

*(Пояснення: Copilot створює технічні файли-підказки для кожного етапу, щоб можна було запускати їх окремо.)*

---

## **05 – Environment Check & Setup**
**Goal:** Verify Python environment and dependencies.

### 🧠 PROMPT for Copilot
> **Task:** Ensure Python ≥ 3.12. Create/activate `venv`.  
> Check packages: Flask, SQLite3, ReportLab, openpyxl, bcrypt, requests.  
> If missing — append to `requirements.txt`.  
> Print environment confirmation. Do not install automatically.

*(Пояснення: Copilot перевіряє середовище, створює `requirements.txt`, але не встановлює пакети без підтвердження.)*

---

## **06 – Gitignore & Requirements**
**Goal:** Finalize `.gitignore` and `requirements.txt`.

### 🧠 PROMPT for Copilot
> **Task:** Create `.gitignore` excluding: `/venv/`, `/__pycache__/`, `/backup/`, `/instance/`, `/uploads/`, and all `*.db` files.  
> Ensure `requirements.txt` contains one line per dependency.  
> Verify both files exist and print confirmation.

*(Пояснення: Copilot створює технічні файли для коректної роботи git і збереження залежностей.)*

---

## **07 – GitHub Upload Preparation**
**Goal:** Prepare repo for upload to GitHub.

### 🧠 PROMPT for Copilot
> **Task:** Generate a markdown file `/doc/Upload_Instructions.md` containing Git commands to initialize and push repo:  
> ```bash
> git init
> git add .
> git commit -m "Initial VTM MVP commit"
> git branch -M main
> git remote add origin <repo_url>
> git push -u origin main
> ```  
> Do not execute these commands. Output only documentation.

*(Пояснення: Copilot створює інструкцію для ручного завантаження проєкту на GitHub.)*

---

## **08 – Commits & Documentation**
**Goal:** Standardize commits and documentation set.

### 🧠 PROMPT for Copilot
> **Task:** After each stage, commit changes using tags like `#stage1_database_created`.  
> Generate files in `/doc/`: `README.md`, `User_Guide.md`, `Changelog.md`, `Testing_Log.md`.  
> Populate README with project summary and usage instructions.  
> Do not push automatically.

*(Пояснення: Copilot формує структуру документації й шаблони комітів, не відправляючи зміни.)*

---

## **09 – Testing Scripts**
**Goal:** Add automated tests.

### 🧠 PROMPT for Copilot
> **Task:** Create basic unit test files: `test_database.py`, `test_flask_app.py`, and `test_reports.py`.  
> Use `pytest` or `unittest`.  
> Tests should verify DB creation, Flask routes, and report generation.  
> Save logs under `/tests/logs/`.  
> Do not run tests automatically.

*(Пояснення: Copilot створює базові тестові файли й структуру для автоперевірок.)*

---

## **10 – Packaging & Android Compatibility**
**Goal:** Prepare for future BeeWare packaging (APK build).

### 🧠 PROMPT for Copilot
> **Task:** Verify project compatibility with BeeWare (Briefcase).  
> Generate `beeware_config.json` with app metadata.  
> Prepare but do not execute commands:  
> ```bash
> briefcase create android
> briefcase build android
> ```  
> Confirm readiness for future APK packaging.

*(Пояснення: Copilot готує конфігурацію для майбутнього пакування під Android, без виконання збірки.)*

---

✅ **Result:** `Copilot_Plan_VTM.md` now includes precise prompts for each development stage, optimized for direct interaction with GitHub Copilot.

