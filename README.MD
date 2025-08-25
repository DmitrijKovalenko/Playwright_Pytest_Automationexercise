# Playwright Python Automationexercise
This project contains a set of automated tests written in Python using the pytest and Playwright frameworks. The goal of the project is to test the functionality of the Automation Exercise website.

# Features
-Reliable tests: Written using Playwright for interacting with web pages.
-Parallel execution: Uses pytest-xdist to run tests on multiple processes simultaneously.
-Report generation: Creates detailed Allure reports after each run.
-CI/CD automation: Fully integrated with GitHub Actions to automatically run tests on every push to the main branch.
-Cross-browser testing: Tests are run in Chromium, Firefox browsers.

Slack notifications: Sends notifications about test results to Slack.

# Technologies
Python: The main programming language.

pytest: The testing framework.

Playwright: The browser automation library.

pytest-playwright: A plugin for integrating Playwright with pytest.

pytest-xdist: A plugin for parallel test execution.

allure-pytest: A tool for creating visual reports.

GitHub Actions: A CI/CD system for automation.

# Project Setup
Follow these steps to run the tests locally on your computer.

1.Clone the repository:
git clone https://github.com/DmitrijKovalenko/Playwright_Pytest_Automationexercise.git
cd Playwright_Pytest_Automationexercise

2.Create and activate a virtual environment:
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Install Playwright browsers:
playwright install --with-deps

# Running Tests

Run all tests using:
pytest

# Running with parameters

Run on a specific browser:
pytest --browser=chromium
Available browsers: chromium, firefox.

Parallel run:
pytest -n 2

Run with Allure Report:
pytest --alluredir=allure-results

# Allure Reports
To view the Allure report locally, run the following command after running the tests:
allure serve allure-results








