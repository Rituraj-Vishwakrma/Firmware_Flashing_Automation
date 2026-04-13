# ⚡ UPS Firmware Flashing Automation:

## 📌 Overview

This project automates the **UPS firmware flashing validation** using `pytest` and `allure reporting`.

It verifies:

* Firmware version
* Hardware revision
* Flashing time
* Flashing logs
* Overall flashing status

---

## 🛠️ Tech Stack

* Python
* Pytest
* Allure Reports

---

## 📂 Project Structure

```
project/
│── tests/
│   └── test_ups_flashing.py
│── ups_flashing.py
│── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd <your-project>
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Test

Run the test using pytest:

```
pytest -m flash --alluredir=allure-results
```

---

## 📊 Generate Allure Report

```
allure serve allure-results
```

---

## 🧪 Test Description

The test validates UPS firmware flashing:

* Calls `ups_flashing()` function
* Captures:

  * Firmware Version
  * Hardware Revision
  * Flashing Time
  * Logs
* Attaches all details to Allure report
* Verifies flashing success

---

## 📌 Test Code Example

```python
def test_ups_flashing():
    result = ups_flashing()
    assert result["status"], "UPS flashing failed"
```

---

## 📎 Allure Attachments

The test includes:

* Firmware version
* Hardware revision
* Flashing duration
* Logs

---

## ✅ Expected Result

* Test should pass if flashing is successful
* All details should appear in Allure report

---

## ⚠️ Notes

* Ensure device is connected before running test
* Make sure firmware files are available
* Run in controlled environment

---

## 👨‍💻 Author

Rituraj Vishwakarma
