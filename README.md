
# 📊 Café ETL Project

A simple Extract-Transform-Load (ETL) pipeline built for a local café chain to help them transition from a paper-based order recording system to a structured SQL Server 2022 database, using Python, Docker, and both CLI & GUI interfaces.

---

## 📦 Tech Stack

- **Language**: Python 3.10+
- **Database**: SQL Server 2022 (via Docker)
- **UI**: CLI + Tkinter GUI
- **Libraries**: `pandas`, `pyodbc`, `python-dotenv`, `tkinter`
- **Tools**: Docker, GitHub, VS Code

---

## 🏗️ Folder Structure

```
cafe_etl_project/
│
├── data/                   # Sample input CSV files
├── database/
│   ├── init.sql            # SQL schema for Orders table
│   └── sql_config.env      # Optional local DB credentials
│
├── docker/
│   └── docker-compose.yml  # SQL Server 2022 setup
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── ui/
│   ├── cli.py              # Text-based menu
│   └── gui.py              # Tkinter GUI
│
├── .env                    # Environment variables (DB connection)
├── etl.log                 # Auto-generated log file
├── main.py                 # App entry point
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run

### 1. 🐳 Start SQL Server via Docker

```bash
docker-compose -f docker/docker-compose.yml up -d
```

### 2. 🧰 Set Up Your Python Environment

```bash
pip install pandas pyodbc python-dotenv
```

> Ensure ODBC Driver 17 or 18 for SQL Server is installed on your system.

### 3. 🧾 Create the Database & Table

Open a terminal and run:

```bash
sqlcmd -S localhost -U sa -P YourStrong!Passw0rd
```

Then run:

```sql
:r database/init.sql
```

Or paste the contents of `init.sql` manually.

---

## 🚀 Run the App

### 🖥️ CLI Version
```bash
python main.py
```

### 🪟 GUI Version

In `main.py`, use:

```python
from ui.gui import run_gui
run_gui()
```

Then run:

```bash
python main.py
```

---

## ✅ Features

- ✅ Extracts order data from any `.csv` file
- ✅ Cleans malformed or incomplete records
- ✅ Removes sensitive PII fields
- ✅ Loads cleaned data into SQL Server 2022
- ✅ CLI and GUI interfaces
- ✅ Export cleaned data to `output.csv`
- ✅ Logs all major actions to `etl.log`

---

## ✏️ Example CSV Format

```csv
Customer Name,Drink,Qty,Price,Branch,Payment Type,Card Number,Date/Time
Dave,Latte,2,3.50,Epsom,Card,1234567812345678,2024-08-12 09:30
```

---

## 📚 Client Deliverables

- ✔️ **Product Demo**: ETL working via CLI & GUI
- ✔️ **Client Presentation**: Benefits of digitisation (e.g. speed, reporting, security)
- ✔️ **Whiteboard Session**: Architecture, alternatives, design decisions

---

## 🔒 Notes

- Default DB password: `YourStrong!Passw0rd`
- `.env` is used for local credentials
- `Card Number` and `Customer Name` are stripped during transform for privacy

---

## 🧠 Reflections

- Built modular ETL structure using Python best practices
- Deployed portable SQL Server using Docker
- Supported both CLI and GUI to match client expectations
- Incorporated logging and error handling for reliability
