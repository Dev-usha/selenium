# Selenium Web Automation Capstone Project

## Automate a Web Application Using Selenium WebDriver with Python

### 🎥 Demonstration Video

[▶ Watch the Capstone Demonstration Video](https://drive.google.com/file/d/14pQC-84tcvic0OHKv8hTeNWyRkupHM6m/view?usp=drivesdk)

> The demonstration video shows the complete Selenium automation workflow and test execution.

---

## 📌 Project Overview

This capstone project demonstrates web application automation using **Selenium WebDriver with Python and Pytest**.

The automation is performed on the **TutorialsNinja Demo** e-commerce application and covers a complete product purchase workflow, including:

* User login
* Product search
* Product selection
* Adding a product to the shopping cart
* Updating product quantity
* Cart verification
* Popup/alert handling
* Screenshot capture
* HTML test report generation

Test data is maintained separately in a JSON file for easy maintenance and reuse.

---

## 🌐 Application Under Test

**TutorialsNinja Demo**

[https://tutorialsninja.com/demo/](https://tutorialsninja.com/demo/)

---

## 🛠️ Technologies Used

| Technology             | Purpose                       |
| ---------------------- | ----------------------------- |
| **Python**             | Programming language          |
| **Selenium WebDriver** | Web browser automation        |
| **Pytest**             | Test execution and validation |
| **Pytest-HTML**        | HTML test report generation   |
| **JSON**               | Test data management          |
| **Google Chrome**      | Browser used for automation   |

---

## 📂 Project Structure

```text
selenium_pm/
│
├── 01_Initial_Lab_Work_and_Video_Demonstrations/
│
├── 02_Capstone_Project/
│   │
│   ├── Source_Code/
│   │   ├── test_ecommerce.py
│   │   ├── requirements.txt
│   │   └── testdata.json
│   │
│   ├── Capstone_Project_Report.pdf
│   │
│   ├── Outputs/
│   │   └── report.html
│   │
│   ├── Screenshots/
│   │   ├── cart_verification.png
│   │   └── test_failure.png
│   │
│   └── Demo_Video.txt
│
├── 03_Certificates/
│
├── .gitignore
└── README.md
```

### Folder Description

| Folder/File                                     | Description                                                    |
| ----------------------------------------------- | -------------------------------------------------------------- |
| `01_Initial_Lab_Work_and_Video_Demonstrations/` | Contains initial lab work and video demonstrations             |
| `02_Capstone_Project/`                          | Contains all capstone project materials                        |
| `Source_Code/`                                  | Contains Selenium automation code, dependencies, and test data |
| `Capstone_Project_Report.pdf`                   | Contains the capstone project report                           |
| `Outputs/`                                      | Contains the generated HTML execution report                   |
| `Screenshots/`                                  | Contains screenshots captured during test execution            |
| `Demo_Video.txt`                                | Contains the demonstration video link                          |
| `03_Certificates/`                              | Contains earned course and project certificates                |

---

## 🧪 Test Data

Test data is maintained in:

```text
02_Capstone_Project/Source_Code/testdata.json
```

The JSON file contains:

* Application URL
* Username
* Password
* Product name
* Product quantity

Example:

```json
{
    "url": "https://tutorialsninja.com/demo/",
    "username": "YOUR_EMAIL_HERE",
    "password": "YOUR_PASSWORD_HERE",
    "product": "MacBook",
    "quantity": 2
}
```

> **Security Note:** Actual passwords or other sensitive credentials should not be committed to a public GitHub repository.

---

## 🔄 Automated Test Workflow

The Selenium test performs the following steps:

1. Launches Google Chrome.
2. Opens the TutorialsNinja Demo application.
3. Navigates to the Login page.
4. Reads test data from the JSON file.
5. Logs into the application.
6. Searches for the specified product.
7. Selects the required product.
8. Adds the product to the shopping cart.
9. Handles the cart notification when displayed.
10. Opens the shopping cart.
11. Updates the product quantity.
12. Verifies the product quantity.
13. Verifies the expected product in the cart.
14. Captures a screenshot of the cart verification.
15. Handles the available alert/popup.
16. Generates the HTML execution report.

---

## ⚙️ Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/Dev-usha/selenium_pm.git
```

### 2. Navigate to the Project

```powershell
cd selenium_pm
```

### 3. Create a Virtual Environment

```powershell
python -m venv venv
```

### 4. Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```powershell
pip install -r 02_Capstone_Project\Source_Code\requirements.txt
```

---

## ▶️ Running the Test

Navigate to the source-code directory:

```powershell
cd 02_Capstone_Project\Source_Code
```

Run the Selenium test:

```powershell
python -m pytest test_ecommerce.py -v
```

---

## 📊 Generate the HTML Test Report

To execute the test and generate the HTML report:

```powershell
python -m pytest test_ecommerce.py -v --html=..\Outputs\report.html --self-contained-html
```

The generated report will be available at:

```text
02_Capstone_Project/Outputs/report.html
```

To open the report:

```powershell
start ..\Outputs\report.html
```

---

## 📸 Test Evidence

### Cart Verification

```text
02_Capstone_Project/Screenshots/cart_verification.png
```

This screenshot provides evidence of the cart verification step.

### Test Failure Screenshot

```text
02_Capstone_Project/Screenshots/test_failure.png
```

This screenshot records the test state when a failure occurs.

---

## ✅ Verification

The automation verifies:

* Successful login
* Correct product selection
* Product added to the cart
* Updated product quantity
* Expected product present in the cart
* Screenshot capture
* Alert/popup handling
* Successful test execution
* HTML report generation

---

## 📈 Test Result

The final test execution result is available in:

```text
02_Capstone_Project/Outputs/report.html
```

The completed test execution resulted in:

```text
1 passed
```

---

## 📦 Project Deliverables

The capstone repository contains:

* Selenium WebDriver automation source code
* JSON-based test data
* Python dependency file
* Capstone project report
* HTML execution report
* Test execution screenshots
* Demonstration video link
* Project documentation

---

## 📝 Conclusion

This project demonstrates the automation of an e-commerce workflow using **Selenium WebDriver with Python and Pytest**.

The implementation covers browser automation, login, product search, product selection, shopping-cart operations, test-data handling, validation, popup/alert handling, screenshot capture, and HTML test reporting.

---

## 🔗 GitHub Repository

**Repository:**

[https://github.com/Dev-usha/selenium_pm](https://github.com/Dev-usha/selenium_pm)
