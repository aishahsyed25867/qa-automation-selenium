# Automated UI Testing with Selenium WebDriver & Python

An end-to-end automated UI regression test for e-commerce login functionality using **Python** and **Selenium WebDriver**. This project automates browser actions to validate successful authentication, user redirection, and session routing on the SauceDemo application.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3
* **Automation Framework:** Selenium WebDriver
* **Target Application:** SauceDemo (E-Commerce Web Application)
* **IDE / Version Control:** VS Code, Git, GitHub

---

## 🧪 Test Case Coverage

| Test ID | Scenario | Execution Steps | Expected Result | Pass/Fail Condition |
| :--- | :--- | :--- | :--- | :--- |
| **TC-001** | Valid User Login | 1. Launch Chrome<br>2. Navigate to SauceDemo<br>3. Input valid credentials<br>4. Click Login | Redirected to `/inventory.html` | Script asserts URL contains `inventory.html` |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed
* Google Chrome browser installed

### Local Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aishahsyed25867/qa-automation-selenium.git](https://github.com/aishahsyed25867/qa-automation-selenium.git)
   cd qa-automation-selenium
   ```

2. **Set up virtual environment & dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   pip install selenium
   ```

3. **Run the test script:**
   ```bash
   python test_login.py
   ```

---

## 📂 Project Structure

```text
qa-automation-selenium/
├── test_login.py      # Automated Selenium test script
├── .gitignore         # Ignores venv and system files
└── README.md          # Project documentation
```