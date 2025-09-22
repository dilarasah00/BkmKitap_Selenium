# Bkm Kitap Web Test Automation Project

This project includes **UI test cases** for the [**Bkm Kitap**](https://www.bkmkitap.com/) website. 

The test strategy includes a combination of **manual and automated testing**:  
- All critical functionalities were first manually tested to ensure they work as expected.  
- Test cases that passed manual verification were selected for **automation**, and the automation process is ongoing for some scenarios.  
- For newly added features (phone number login and password reset via phone), **Smoke and Regression Tests** were executed to verify that:  
  - The new functionalities work correctly. Although phone number login works correctly, the error message for invalid/empty input still shows the email-related message, which is reported as a minor issue.  
  - Existing features are not negatively affected by these additions.  

The main functionalities covered in this project include:  
- **Login** (email and phone number login)  
- **Password reset** (via email and phone)  
- **Search**  
- **Filter**  
- **Cart**   

## Tech Stack
- **Language:** Python  
- **Frameworks:** Pytest, Selenium  
- **Design Pattern:** Page Object Model (POM)  
- **Test Data:** JSON-based  


# Project Folder Structure
```
BkmKitap/
├──config/
│ ├── get_json_file.py 
│ └── util.py
├── data/
│ ├── filter_data_for_search_input.json
│ ├── invalid_login_data.json
│ ├── search_data.json
│ ├── status_messages.json
│ ├── suggestion_test_data.json
│ └── valid_login_data.json 
├── pages/
│ ├── base_page.py
│ ├── filter_page.py
│ ├── login_page.py
│ └── search_page.py
│
├── tests/
│ ├── negative_tests
│ │  ├── test_invalid_login.py
│ │  └── test_search.py
│ ├── positive_tests
│ │  ├── test_filter.py
│ │  ├── test_login.py
│ │  ├── test_search.py
│ │  └── test_suggestion.py
│
├── requirements.py 
├── test_document/
│  ├── Test_plan V2.0
│  ├── Test_plan V1.0
│  ├── bug_report.xlsx
│  └── test_cases_and_result.xlsx
└── conftest.py 
```


## About Document 
- All manual and automated test cases, along with their results, are documented in `test_document/test_cases_and_result.xlsx`.
- Found bugs are documented in `test_document/bug_report.xlsx`.
- Test Plan for the first version is documented in `test_document/Test_plan V1.0`.
- Test Plan for smoke and regression testing is documented in `test_document/Test_plan V2.0`.


## 🧪 Running the Test Cases

### 1️⃣ Prepare the environment
 
Clone the project and install the dependencies to run tests:

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install required packages
pip install -r requirements.txt
```
---

### 2️⃣ Running the tests

Run all tests:

```bash
pytest tests
```

Run a specific test (e.g., test_search.py under the negative_tests folder):

```bash
pytest tests/negative_tests/test_search.py
```


## ⚠️ Important Note

- The `valid_login_data.json` file is intentionally empty.  
- If you want to run **valid login test cases** or execute **all test cases together**, you need to add real credentials into `data/valid_login_data.json`.

