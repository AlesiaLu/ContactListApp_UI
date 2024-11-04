# ContactListApp_UI
ContactListApp_UI
### Project Overview
This project automates UI testing for the Contact List App .

### Project Structure
- **locators/**: Contains element locators for each page, grouped by page-specific locator files for easy maintenance.
- **pages/**: Contains files for each page of the web application, with methods representing user actions (e.g., filling forms, clicking buttons, verifying elements).
- **tests/**: Contains test files for each page, validating the logic and interactions defined in the corresponding page files.
- **results/**: Stores Allure reports generated after each test run, providing a detailed view of test results and insights.
- 
### Tech Stack
- **Python**
- **Selenium WebDriver**
- **pytest** for running tests and generating reports
- **Allure** for comprehensive test reporting

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AlesiaLu/ContactListApp_UI.git
    ```

2. **Install dependencies**:
    Ensure you have Python and pip installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    Execute all tests using **pytest**:
    ```bash
    pytest
    ```

4. **Generate a test report**:
    To create a detailed Allure report, run:
    ```bash
    pytest --alluredir=result
    allure serve result
    ```
    Or To create HTML-report с pytest-html, run:
    pytest ./tests --html=report.html

### Example Usage
To run a specific test, specify the test file path:
```bash
pytest tests/test_login.py
```
This runs the test suite for the login page, ensuring that functionalities like successful login and error messaging work as expected.
