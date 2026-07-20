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

#### 🔹 TC-001: Valid User Login
* **Target Application:** SauceDemo (`https://www.saucedemo.com/`)
* **Test Objective:** Verify that a standard user can log in with valid credentials and navigate to the inventory page.
* **Execution Steps:**
  1. Launch Chrome Browser.
  2. Navigate to SauceDemo login page.
  3. Enter username (`standard_user`) and password (`secret_sauce`).
  4. Click the **Login** button.
  5. Assert the post-login URL contains `inventory.html`.
* **Expected Result:** User redirected to `/inventory.html`.
* **Status:** PASS

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
   pip install selenium pytest
   ```

3. **Run the test script:**
   ```bash
   python3 test_login.py
   ```

---

## 📂 Project Structure

```text
qa-automation-selenium/
├── test_login.py      # Automated Selenium test script
├── .gitignore         # Ignores venv and system files
└── README.md          # Project documentation
```