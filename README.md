# Bkm Kitap Web Test Automation Project

This project includes **UI test cases** for the [**Bkm Kitap**](https://www.bkmkitap.com/) website. 

The covered functionalities are:  
- **Login**  
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
├── testcases/
│  └── test_cases_and_result.xlsx
└── conftest.py 
```

> ℹ️ **Note:** All manual and automated test cases, along with their results, are documented in `testcases/test_cases_and_result.xlsx`.

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

Run a spesific test (e.g., test_search.py under the negative_tests folder):

```bash
pytest tests/negative_tests/test_search.py
```


## ⚠️ Important Note

- The `valid_login_data.json` file is intentionally empty.  
- If you want to run **valid login test cases** or execute **all test cases together**, you need to add real credentials into `data/valid_login_data.json`.

