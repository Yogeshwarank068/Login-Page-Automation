# Login Page Automation Framework 

A clean, maintainable web automation framework built with Python, Selenium WebDriver, and Pytest.
This project implements the **Page Object Model (POM)** design pattern to automate authentication testing against 
the [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) playground.

---

## Features

- **Page Object Model (POM):** Clean separation of test scripts and page locators/interactions for easy maintenance.
- **Pytest Architecture:** Leverages reusable fixtures (`conftest.py`) for clean browser startup and teardown lifecycles.
- **Smart Synchronization:** Implements explicit waits to handle dynamic web elements cleanly without flaky hardcoded sleeps.
- **Cross-Browser Ready:** Pre-configured for Microsoft Edge via Selenium WebDriver (easily extensible to Chrome, Firefox, or headless runs).

---

## Project Structure

Login-Page-Automation/
├── pages/
│   ├── __init__.py
│   └── login_page.py       # Page locators and user actions
├── tests/
│   ├── __init__.py
│   └── test_login.py       # Test assertions and scenarios
├── conftest.py             # driver setup/teardown
├── pytest.ini              # Pytest runner configuration
├── .gitignore              # Files excluded from version control
└── README.md               # Project documentation
