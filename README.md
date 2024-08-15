# API testing with pytest

This repository contains a simple pytest script to execute API automation test for jsonplaceholder.typicode.com

## Project Structure
```bash
pytestAPI/
│
├── logs/              # Log files generated during tests
├── reports/           # HTML reports generated after tests
├── schemas/           # JSON schema files for validation
│   └── {schema}.json
├── tests/             # Test files
│   └── {test}.py
├── config.py          # Configuration file (Base URL, Report path)
├── conftest.py        # Pytest configuration and report customization
├── requirements.txt   # Required Python packages
└── run.py             # Automate installation, execute test and generate report
```

## Getting Started

### Requirements
- python (I'm using version 3.12.5)
- pip (I'm using version 24.2)

>  In case there is an issue during the installation or during the run process, it might be worth updating the version to match mine.

### Dependencies
All packages has been listed in `requirements.txt`. List of the packages used in this project are:
- pytest
- requests
- jsonschema
- pytest-html

### Configuration
To change the base URL or report path, you can change the value `BASE_URL` and `REPORT_PATH` in `config.py`.
- Base URL: The base URL for the API
- Report Path: The path and file name for the HTML report

### Set Up Virtual Environment (Optional)
Since this project is just as simple pytest script, it is not extremely needed to run in virtual environment. But, in case you want to run this project in an isolated virtual environment, please follow [this documentation](https://docs.python.org/3/library/venv.html#module-venv) to setup and activate virtual environment in python.

### Manual installation
> If you want to skip manual installation and use the `run.py` to automate packages installation and test execution, you can skip this part.

Make sure you have Python installed. Then execute this command to install required packages that listed in the requirements.txt:
```bash
pip install -r requirements.txt
```

## How to run
### Running the test 
To run the test and directly show the html report, you can use the `run.py` script:
```bash
python run.py
```
This script will:
1. Check if the required packages are installed.
2. Install missing packages (if any).
3. Execute the tests.
4. Open the generated HTML report in your default web browser.

### Manually run the test
- To run the test using the default command, you can execute this command:
```bash
pytest
```

### Report
- Once the test has run, you will see 2 new directories (`logs` and `report`). To open the HTML report, navigate to `reports` directory and open the `test-report.html` file in your browser.
- To customize the html report title, you can adjust it in `conftest.py`.

## Screenshot of test results
![](https://raw.githubusercontent.com/ghufronalwi/PytestAPITest/master/ss-pytest-cli.png)
![](https://raw.githubusercontent.com/ghufronalwi/PytestAPITest/master/ss-pytest-html-report.png)
