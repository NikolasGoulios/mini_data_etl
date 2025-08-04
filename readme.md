# 🧼 Week 1 – Mini Project 1: mini_data_etl

**Goal:** Build a simple yet robust CSV cleaning tool for Airbnb listing data, or any other data.

---

## 📂 Project Structure

```
Week_01_Mini_Data_ETL/
├── data/
│   ├── raw/                         # Unprocessed raw CSVs
│   ├── clean/                       # Successfully cleaned data
│   └── dropped/                     # Rows removed due to invalid or missing data
├── scripts/
│   └── clean.py                     # Main cleaning script
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git exclusion rules
├── Makefile                        # Automation shortcuts
└── README.md
```

---

## ⚙️ Features

- Drops rows with nulls in **important columns**: `['name', 'price']`
- Cleans `price` column by:
  - Removing `$` and `,`
  - Converting to float
- Drops rows with invalid prices
- Calculates `price_per_bedroom`
- Removes duplicates
- Saves:
  - Cleaned CSV → `data/clean/`
  - Dropped rows → `data/dropped/`

---

## 🚀 How to Run

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the cleaner

```bash
make run
make help
```

---

## 🔄 Output

- ✅ Cleaned CSV: `data/clean/Clean_Barcelona_Airbnb_Listing_2025.csv`
- ❌ Dropped rows: `data/dropped/Dropped_Barcelona_Airbnb_Listing_2025.csv`

---

## 💡 Notes

- You can modify `IMPORTANT_COLUMNS` in `clean.py` to fit other datasets
- Makefile support available (run `make clean`)
- Future improvements: Logging, test coverage, CLI options

---

## 📚 Learnings

This mini-project teaches:

- Basic ETL-style CSV cleaning
- Working with `pandas` for data transformations
- Writing reusable and readable scripts
- Automating data workflows locally

---
