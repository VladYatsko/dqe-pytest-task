# dqe_pytest_automation_framework

## About this framework:
Current framework was created to test functionality of TRN database. Current framework was created using Python.

## How to run tests:
First of all you need to install all the dependencies:
```
pip install -r requirements.txt
```

After all the actions above are performed you can run tests with three ways:
1) With default Python commands from framework root folder: 
```
pytest --alluredir=results --reruns 5 .\tests\   
```
After tests are finished you need to run:
```
allure serve results 
```
To generate allure report.

2) With running test_runner.bat for Windows to avoid typing commands 2 times.
3) For Unix/macOS there is test_runner.sh file, but to run it you need first run
```bash
chmod +x ./test_runner.sh
```
Then execute file with similar snippet as for Windows OS.
