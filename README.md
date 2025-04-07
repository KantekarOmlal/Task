# 🧼 Task 1: Data Cleaning and Preprocessing

## 📋 Internship Task Description
**Objective:** Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats).  
**Tools Allowed:** Excel / Python (Pandas)  
**Deliverables:** Cleaned dataset + short summary of changes

---

## Done
- Handle missing values using `.isnull()` in Python
- Remove duplicate rows with `.drop_duplicates()`
- Standardize text (e.g., gender, neighborhood names)
- Convert date formats to consistent `datetime`
- Rename column headers to snake_case (lowercase, no spaces)
- Fix data types (e.g., `age` as int, `scheduled_day` as datetime)

---

## Dataset Chosen
**Medical Appointment No Shows** 
Contains patient health, appointment, and attendance information.

---

## ✅ Cleaning Steps Performed

1. **Renamed columns**: snake_case format and corrected typos  
   - `Hipertension` → `hypertension`  
   - `Handcap` → `handicap`  
   - `No-show` → `no_show`  

2. **Converted date columns** to `datetime` format  
   - `ScheduledDay` → `scheduled_day`  
   - `AppointmentDay` → `appointment_day`  

3. **Standardized text data**  
   - `gender` → uppercased  
   - `no_show` → capitalized  

4. **Removed duplicates** using `.drop_duplicates()`

5. **Checked for missing values** — None found

6. **Dropped invalid ages** (e.g., negative values)

7. **Validated data types** for consistency

---

## Files Included

| File Name                      | Description                             |
|-------------------------------|-----------------------------------------|
| `KaggleV2-May-2016.csv`       | Raw dataset                             |
| `task1.py`                    | Python script for cleaning              |
| `cleaned_medical_appointments.csv` | Final cleaned dataset                  |
| `README.md`                   | Documentation (this file)               |

---

## 🛠 Tools Used

- Python 3.x
- Pandas
