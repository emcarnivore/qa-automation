# QA Automation with Selenium & Python

## 📌 Project Overview

This project is a **QA Automation** framework using **Selenium with Python**. It follows the **Page Object Model (POM)** to improve test maintainability and readability.

## 📝 Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python Package Installer)

### Setting Up the Project

1. **Clone the Repository**
   ```git clone <repository-url>```
   ```cd qa-automation```

2. **Create a Virtual Environment**
   ```python3 -m venv venv```

3. **Activate the Virtual Environment**
   On macOS and Linux:
   ```source venv/bin/activate```
   On Windows:
   ```.\venv\Scripts\activate```

4. **Install Required Packages**
   ```pip install -r requirements.txt```

   requirements.txt:
   - pytest
   - selenium
   - webdriver-manager

### Running Tests

1. **Run Tests with PyTest**
   ```pytest tests/```

2. **Generate HTML Report (optional)**
   ```pytest --html=reports/report.html```

### Additional Notes

- Ensure that your IDE (e.g. Visual Studio Code) is configured to use the virtual environment's interpreter.

- **To Deactivate the Virtual Environment**
```deactivate```

## 🏗️ Folder Structure Explained

- **config/** → Stores framework configuration settings.
- **data/** → Holds test data for various test cases.
- **locators/** → Defines element locators for different pages.
- **pages/** → Implements the **Page Object Model (POM)** to separate UI interactions.
- **reports/** → Stores test execution reports.
- **screenshots/** → Saves screenshots of failed test cases for debugging.
- **tests/** → Contains automated test scripts following PyTest conventions.
- **utils/** → Utility functions and configuration loaders.
- **venv/** → Virtual environment directory containing project-specific dependencies.
- **root files:**
  `.env` → Stores environment-specific settings.
  `.gitignore` → Specifies files and folders to exclude from version control.
  `pytest.ini` → PyTest configuration file for test execution settings.
  `requirements.txt` → Lists required Python dependencies for the project.

## 📜 License

This project is licensed under the GPL-3.0 License.

